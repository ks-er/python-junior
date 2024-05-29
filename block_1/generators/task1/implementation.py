def fib(number):
    num1 = 1
    yield num1
    num2 = 1
    yield num2

    for i in range(number - 2):
        num1, num2 = num2, num1 + num2
        yield num2
