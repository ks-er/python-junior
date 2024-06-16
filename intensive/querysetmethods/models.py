from django.db import (
    models,
)
from django.db.models import Q, Count


class Product(models.Model):
    """
    Товар
    """
    name = models.CharField('Наименование', max_length=300)

    class Meta:
        db_table = 'product'
        app_label = 'admin'


class ProductCount(models.Model):
    """
    Количество товара
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    begin = models.DateField('Начало периода')
    end = models.DateField('Окончание периода')
    value = models.PositiveIntegerField('Значение')

    class Meta:
        db_table = 'product_count'
        app_label = 'admin'


class ProductCost(models.Model):
    """
    Стоимость товара
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    begin = models.DateField('Начало периода')
    end = models.DateField('Окончание периода')
    value = models.DecimalField('Значение', max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'product_cost'
        app_label = 'admin'


class Customer(models.Model):
    """
    Покупатель
    """
    name = models.CharField('Покупатель', max_length=300)

    class Meta:
        db_table = 'customer'
        app_label = 'admin'


class Order(models.Model):
    """
    Заказ
    """
    number = models.CharField('Номер', max_length=50)
    date_formation = models.DateField('Дата')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Покупатель')

    class Meta:
        db_table = 'order'
        app_label = 'admin'


class OrderItem(models.Model):
    """
    Позиция заказа
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар')
    count = models.DecimalField(verbose_name='Количество', max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'order_item'
        app_label = 'admin'


def get_order_count_by_customer(name):
    """Возвращает количество заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    q_customer = Q(customer__name=name)
    query = Order.objects.all().select_related('customer', 'customer__name').filter(q_customer)

    return query.count()

def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    q_start_date = Q(order__date_formation__gte=begin)
    q_end_date = Q(order__date_formation__lte=end)

    max_order = (Customer.objects.annotate(
        period_orders=Count('order', filter=q_start_date & q_end_date)
        ).order_by('-period_orders'))[:1]

    res = max_order.values_list('name', 'period_orders')

    if res[0][1] > 0:
        return res[0]
    else:
        return None

def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """
    q_start_date = Q(date_formation__gte=begin)
    q_end_date = Q(date_formation__lte=end)

    query = Order.objects.all().filter(q_start_date & q_end_date)
    raise NotImplementedError

def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    raise NotImplementedError

def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    raise NotImplementedError