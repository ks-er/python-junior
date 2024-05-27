import time

from block_1.common import (
    MyException,
)

def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def decorator_fn(function):        
        def wrapper(*args, **kwargs):
            for i in range (times):
                try:
                    result = function(*args, **kwargs)
                    if (validate_result(result)):
                        return result
                    else:
                        time.sleep(delay)
                except:
                    time.sleep(delay)

            raise MyException
        return wrapper
    return decorator_fn

def validate_result(result):
    return True
