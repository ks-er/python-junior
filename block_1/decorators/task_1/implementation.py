import time

def time_execution_decorator(function):
    """
    Обертка, печатающая время выполнения функции.
    """

    def wrapper(arg):
        global start_time
        if (arg < 0 or type(arg) != int):
             return "0s"

        result = function(arg)
        return str(time.time() - start_time) + "s"

    return wrapper

@time_execution_decorator
def get_factorial(num):

    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

start_time = time.time()
print(get_factorial(5))
