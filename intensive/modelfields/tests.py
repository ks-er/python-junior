
from datetime import (
    date,
)

from django.test import (
    TestCase,
)

from modelfields.models import (
    Department,
    Worker
)

class WorkerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods

        department = Department.objects.create(
            name='Отдел №1'
        )
        workers = [
            Worker(
                first_name='Новый',
                last_name='Новый',
                startwork_date=date(2021, 1, 1),
                department=department),
            Worker(
                first_name='Неизвестный',
                department=department
            ),
            Worker(
                first_name='Владимиров',
                last_name='Владимир',
                startwork_date=date(2021, 1, 1),
                tab_num=11,
                department=department
            ),
            Worker(
                first_name='Алексеев',
                last_name='Алексей',
                startwork_date=date(2021, 1, 1),
                tab_num=1,
                department=department
            )
        ]

        Worker.objects_all.bulk_create(workers)

    @classmethod
    def test_all_count_workers(cls):
        all_count = Worker.objects_all.all().count()
        return str(all_count) + ":" + str(all_count == 4)

    @classmethod
    def test_all_active_count_workers(cls):
        active_count = Worker.objects.all().count()
        return str(active_count) + ":" + str(active_count == 2)

    @classmethod
    def test_get_active_worker_count(cls):
        department = Department.objects.filter(name='Отдел №1').first()
        kol = department.get_active_worker_count
        return str(kol) + ":" + str(kol == 2)

    @classmethod
    def test_get_all_worker_count(cls):
        department = Department.objects.filter(name='Отдел №1').first()
        kol = department.get_all_worker_count
        return str(kol) + ":" + str(kol == 4)