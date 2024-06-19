from django.shortcuts import render

from metaandinheritance.tests import WorkerModelTest

def index(request):
    #WorkerModelTest.setUpTestData()
    #WorkerModelTest.setUpTestData1()

    listTask = [
        WorkerModelTest.test_all_count_workers(),
        WorkerModelTest.test_count_only_workers(),
        WorkerModelTest.test_ordered_worker_model(),
        WorkerModelTest.test_department_office(),
        WorkerModelTest.test_worker_status()
    ]

    listTask4 = [
        WorkerModelTest.test_department_office()
    ]

    return render(
            request,
            'metaandinheritance.html',
            context={
                'listTask': listTask,
                'listTask4': listTask4,
            }
    )