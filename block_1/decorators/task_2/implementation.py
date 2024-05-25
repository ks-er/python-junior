from block_1.common import (
    MyException,
)

def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    def wrapper(number):
        if (isinstance(number, int) and number >= 0):
            return function(number)
        else:
            return MyException

    return wrapper

def cache_value(function):
    """
    Обертка, которая будет кэшировать результат. 
    Обертка должна значительно ускорить получение результата по повторно переданному значению  
    """

    def wrapper(number):
        global cache
        if not(isinstance(number, int)):
            return MyException("Значение должно быть неотрицательным int")
        elif number < 0:
            return MyException("Значение должно быть неотрицательным int")
        elif number in cache:
            return cache[number]
                
        value = function(number)
        cache[number] = value
        return value

    return wrapper

cache =  {}
