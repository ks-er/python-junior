from django.shortcuts import render

from middlewares.tests import MiddlewareTestCase

def index(request):

    listTask1 = [
        #MiddlewareTestCase.test_FormatterMiddleware(),
        #MiddlewareTestCase.test_default_FormatterMiddleware(),
        #MiddlewareTestCase.test_CheckErrorMiddleware(),
        #MiddlewareTestCase.test_default_CheckErrorMiddleware()
    ]

    return render(
            request,
            'middlewares.html',
            context={
                'listTask1': listTask1,
            }
    )