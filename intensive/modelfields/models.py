from django.db import models
from django.db.models import Manager, Q, Count, F


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):

        """
        Переопределенный кверисет с фильтрацией сотрудников с заданной датой принятия на работу и с не пустым табельным номером отличным от 0
        """
        return super().get_queryset().filter(tab_num__gt=0,startwork_date__isnull=False)

    def get_workers_info(self):
        """
            Получение  списка строк в которых содержится
        фамилия, имя, табельный номер сотрудника а также название подразделения в котором числится
        Строки упорядочены по фамилии и имени сотрудника.
        Каждая строка должна быть в формате вида: Васильев Василий, 888, Подразделение №1
        """
        query = Worker.objects.all().select_related('department').order_by('first_name', 'last_name')

        res_list = list()
        for worker in query:
            res_list.append(
                list([
                    " ".join([worker.first_name, worker.last_name]),
                     worker.tab_num,
                     worker.department.name])
            )
        return res_list


class Department(models.Model):
    name = models.CharField('Наименование', max_length=30)

    @property
    def get_active_worker_count(self):
        """
        Количество активных сотрудников подразделения
        """
        q_dep = Q(department=self.id)
        query = Worker.objects.all().select_related('department')
        return query.filter(q_dep).count()

    @property
    def get_all_worker_count(self):
        """
        Количество всех сотрудников подразделения
        """
        q_dep = Q(department=self.id)
        query = Worker.objects_all.all().select_related('department')
        return query.filter(q_dep).count()

    class Meta:
        db_table = 'department'
        app_label = 'admin'


class Worker(models.Model):
    """
    Сотрудник
    """

    objects = WorkerManager()
    objects_all = Manager()

    first_name = models.CharField('Фамилия', max_length=30)
    last_name = models.CharField('Имя', max_length=30)
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'workers'
        verbose_name = 'Сотрудник'
        app_label = 'admin'