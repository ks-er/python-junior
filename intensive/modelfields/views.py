from django.http import HttpResponse, JsonResponse

from modelfields import tests
from modelfields.tests import WorkerModelTest


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    #tests.WorkerModelTest.setUpTestData()

    res1 = WorkerModelTest.test_all_count_workers()
    res2 = WorkerModelTest.test_all_active_count_workers()
    res3 = WorkerModelTest.test_get_active_worker_count()
    res4 = WorkerModelTest.test_get_all_worker_count()
    return HttpResponse(res1 + "<br>" + res2 + "<br>" + res3 + "<br>" + res4)