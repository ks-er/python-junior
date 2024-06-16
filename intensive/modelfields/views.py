from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from modelfields import tests
from modelfields.tests import WorkerModelTest


def index(request):
    res1 = WorkerModelTest.test_all_count_workers()
    res2 = WorkerModelTest.test_all_active_count_workers()
    res3 = WorkerModelTest.test_get_active_worker_count()
    res4 = WorkerModelTest.test_get_all_worker_count()
    res5 = WorkerModelTest.test_get_workers_info()

    return render(
            request,
            'modelfields.html',
            context={
                'res1': res1,
                'res2': res2,
                'res3': res3,
                'res4': res4,
                'items': res5
            }
    )