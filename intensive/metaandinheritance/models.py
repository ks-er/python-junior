from django.db import models
from django.db.models import Q

class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):
        """
        Переопределенный кверисет возвращающий всех сотрудников без директоров
        """
        f_not_dir = Q(director__worker26_ptr_id__isnull=True)
        return super().get_queryset().filter(f_not_dir)


class CommonOffice(models.Model):
    """
    Офис
    """
    address = models.TextField('Адрес')
    mail = models.CharField('Адрес почты', max_length=30)

    class Meta:
        abstract = True


class EducationOffice(CommonOffice):
    """
    Учебный офис
    """
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'education_office'
        app_label = 'admin'


class GeneralOffice(CommonOffice):
    """
    Головной офис
    """
    name = models.TextField('Название головного офиса ')

    class Meta:
        db_table = 'office'
        app_label = 'admin'


class Department26(models.Model):
    """
    Подразделение
    """
    name = models.CharField('Наименование', max_length=30)

    education_office = models.ForeignKey(EducationOffice, on_delete=models.SET_NULL, null=True )
    office = models.ForeignKey(GeneralOffice, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'department26'
        app_label = 'admin'


class Person(models.Model):
    """
    Физическое лицо
    """
    first_name = models.CharField('Фамилия', max_length=30)
    last_name = models.CharField('Имя', max_length=30)

    class Meta:
        abstract = True


class Worker26(Person):
    """
    Сотрудник
    """
    objects = WorkerManager()
    objects_all = models.Manager()
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department26, on_delete=models.CASCADE)

    def get_status(self):
        return f'{self.first_name} работает с {self.startwork_date}'

    class Meta:
        db_table = 'workers26'
        verbose_name = 'Сотрудник'
        app_label = 'admin'


class OrderedWorker(Worker26):
    """
    Модель с  сотрудниками упорядоченными по фамилии и дате приема на работу
    """

    @property
    def startwork_year(self):
        """
        Получить значение года приема на работу
        """
        return self.startwork_date.year

    class Meta:
        proxy = True
        app_label = 'admin'
        ordering = ('first_name', 'startwork_date')


class Director(Worker26):
    """
    Директор
    """
    # что здесь не хватает?
    grade = models.IntegerField('Оценка', default=1)

    class Meta:
        db_table = 'directors'
        verbose_name = 'Директор'
        app_label = 'admin'