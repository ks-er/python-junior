from django.shortcuts import render

from querysetmethods.tests import ProductModelTest

def index(request):
    #ProductModelTest.setUpTestData()

    listTask1 = [
        ProductModelTest.test_oleg(),
        ProductModelTest.test_ivan(),
        ProductModelTest.test_egor(),
        ProductModelTest.test_fedot()
    ]

    listTask2 = [
        ProductModelTest.test_january(),
        ProductModelTest.test_febraury(),
        ProductModelTest.test_march(),
        ProductModelTest.test_april()
    ]

    listTask3 = [
        ProductModelTest.test_price_january(),
        ProductModelTest.test_price_febraury(),
        ProductModelTest.test_price_march(),
        ProductModelTest.test_price_april()
    ]

    listTask4 = [
        ProductModelTest.test_prod_january(),
        ProductModelTest.test_prod_febraury(),
        ProductModelTest.test_prod_march(),
        ProductModelTest.test_prod_april()
    ]

    return render(
            request,
            'querysetmethods.html',
            context={
                'listTask1': listTask1,
                'listTask2': listTask2,
                'listTask3': listTask3,
                'listTask4': listTask4,
            }
    )