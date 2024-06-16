from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from querysetmethods import tests
from querysetmethods.tests import ProductModelTest

def index(request):
    #ProductModelTest.setUpTestData()

    return render(
            request,
            'index.html',
            context={
                'items': []
            }
    )