from django.http import JsonResponse
from django.shortcuts import render

from middlewares.tests import MiddlewareTestCase


def index(request):
    list1 = [
        MiddlewareTestCase.test_FormatterMiddleware(),
        MiddlewareTestCase.test_default_FormatterMiddleware(),
        MiddlewareTestCase.test_CheckErrorMiddleware(),
        MiddlewareTestCase.test_default_CheckErrorMiddleware()
    ]
    print(request.path_info)
    return render(
            request,
            'middlewares.html',
            context={
                'maths': list1
            }
    )

def calc(request):
    """
        Представление которому в параметре запроса maths через разделитель перечисляются простейшие арифметические операции
        например maths=3*3,10-2,10/5
        по умолчанию в качестве символа разделителя выступает сивол запятой.
        В необязательном параметре delimiter указывается символ разделителя арифметических операций
        например calc/?maths=3*3;10-2;10/5&delimiter=;

        Результат:  JsonResponse вида {'3*3': 9, '10-2': 8, '10/5': 2}
        """
    print(request.method)
    if request.method == 'GET':

        maths = request.GET.get('maths', "")
        delimiter = request.GET.get('delimiter', ",")

        if (len(maths) == 0):
            return JsonResponse({})

        print(maths)
        print(delimiter)
        list = Calculator.calculate(maths, delimiter)
        return JsonResponse(list)
    else:
        pass

class Calculator():

    @classmethod
    def calculate(cls, maths, delimiter):
        list = maths.split(delimiter)

        dict = {}
        for item in list:
            if ('+' in item):
                dict[item] = getItemValue(item, '+')
            elif ('-' in item):
                dict[item] = getItemValue(item, '-')
            elif ('*' in item):
                dict[item] = getItemValue(item, '*')
            elif ('/' in item):
                dict[item] = getItemValue(item, '/')
            else:
                dict[item] = item

        return dict

def getValues(str, delimiter):
    return str.split(delimiter)

def getItemValue(item, delimiter):
    values = getValues(item, delimiter)
    if (len(values) != 2):
        return item

    v1 = int(values[0])
    v2 = int(values[1])

    if (delimiter == '+'):
        return v1 + v2
    elif (delimiter == '-'):
        return v1 - v2
    elif ('*' in item):
        return v1 * v2
    elif ('/' in item):
        return v1 / v2
    else:
        return item