count = 0
def counter(function):

    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """
    def wrapper():
        global count
        count+=1
        function()
        return count
        
    return wrapper
