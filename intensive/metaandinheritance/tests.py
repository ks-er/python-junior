from datetime import date

from django.test import (
    TestCase,
)

from metaandinheritance.models import (
    EducationOffice,
    GeneralOffice,
    Director,
    OrderedWorker,
    Department26,
    Worker26,
)


class WorkerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        education_office = EducationOffice.objects.create(
            address='Москва',
            mail='edu@gmail.com'
        )

        general_office = GeneralOffice.objects.create(
            address='Казань',
            mail='general@gmail.com'
        )

        department = Department26.objects.create(
            name='Отдел №1',
            education_office=education_office,
            office=general_office
        )
        workers = [
            Worker26(
                first_name='Новый',
                last_name='Новый',
                startwork_date=date(2009, 3, 3),
                department=department
            ),
            Worker26(
                first_name='Неизвестный',
                department=department
            ),
            Worker26(
                first_name='Владимиров',
                last_name='Владимир',
                startwork_date=date(2011, 11, 11),
                tab_num=2,
                department=department
            ),
            Worker26(
                first_name='Алексеев',
                last_name='Алексей',
                startwork_date=date(2008, 8, 8),
                tab_num=33,
                department=department
            ),
            Worker26(
                first_name='Алексеев',
                last_name='Андрей',
                startwork_date=date(2004, 1, 1),
                tab_num=3,
                department=department
            ),
            Worker26(
                first_name='Алексеев',
                last_name='Андрей',
                startwork_date=date(2009, 9, 9),
                tab_num=2,
                department=department
            ),
        ]

        Worker26.objects_all.bulk_create(workers)

    @classmethod
    def setUpTestData1(cls):
        dep26 = Department26.objects.get(pk=1)

        Director.objects.create(
            first_name='Тарасов',
            last_name='Тарас',
            startwork_date=date(1999, 1, 1),
            tab_num=1,
            department=dep26)

    @classmethod
    def test_all_count_workers(cls):
        all_count = Worker26.objects_all.all().count()
        return {
            'elem': all_count,
            'itog': all_count == 7
        }

    @classmethod
    def test_count_only_workers(cls):
        only_workers = Worker26.objects.all().count()
        return {
            'elem': only_workers,
            'itog': only_workers == 6
        }

    @classmethod
    def test_worker_status(cls):
        worker = Worker26.objects.all().first()
        status = worker.get_status()
        return {
            'elem': status,
            'itog': status == 'Новый работает с 2009-03-03'
        }

    @classmethod
    def test_ordered_worker_model(cls):
        worker = OrderedWorker.objects.all().first()
        return {
            'elem': worker.startwork_year,
            'itog': worker.startwork_year == 2004
        }

    @classmethod
    def test_department_office(cls):
        department = Department26.objects.all().first()
        return (
            {
                'elem': department.education_office.address,
                'itog': department.education_office.address == 'Москва'
            },
            {
                'elem': department.office.address,
                'itog': department.office.address == 'Казань'
            }
        )
