from django.db import (
    models,
)
from django.db.models import Q, F, Count, Sum, OuterRef, Subquery, Max, Value, Case, When


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

    f_start = Q(begin__gte=begin)
    f_end = Q(end__lte=end)

    f_start_date = Q(order__date_formation__gte=begin)
    f_end_date = Q(order__date_formation__lte=end)

    order_item_query = OrderItem.objects.filter(f_start_date & f_end_date)

    f1 = Q(begin__lte=OuterRef("order__date_formation"))
    f2 = Q(end__gte=OuterRef("order__date_formation"))
    f3 = Q(product_id=OuterRef("product_id"))

    products_sudq1 = ProductCost.objects.filter(f_start & f_end).filter(f1 & f2 & f3)

    products_sudq_addit = ProductCost.objects.filter(f_start & f_end).filter(f3).order_by('-end')[:1]

    sum_q = (order_item_query.annotate(
        price = Subquery(products_sudq1.values('value'))
    ))

    sum_q0 = sum_q.annotate(
        all_pr=
            Case(
                When(price__isnull=True, then=Subquery(products_sudq_addit.values('value'))),
                default=F('price'), output_field=models.DecimalField()
            )
    ).annotate(
        summa= F('all_pr') * F('count'))

    query_all_sum = sum_q0.values('order_id','order__number').annotate(all_sum=Sum(F('summa')))

    query_max_sum = query_all_sum.aggregate(max_sum=Max(F('all_sum')))
    f_max_sum = Q(all_sum=query_max_sum['max_sum'])

    itog_query = query_all_sum.filter(f_max_sum)
    res = itog_query.order_by('-order_id')[:1]

    if len(res) > 0:
        return (res[0]['order__number'], res[0]['all_sum'])
    else:
        return None


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """

    f_start_date = Q(order__date_formation__gte=begin)
    f_end_date = Q(order__date_formation__lte=end)
    order_item_query = OrderItem.objects.filter(f_start_date & f_end_date).only('count', 'product_id', 'product__name')

    product_count_query = order_item_query.values('product_id', 'product__name').annotate(
        prod_count=Sum('count')
    )

    query_max_count = product_count_query.aggregate(max_count = Max(F('prod_count')))

    f_count = Q(prod_count=query_max_count['max_count'])
    itog_query = product_count_query.filter(f_count).values('product__name', 'prod_count')

    res_list = list()
    for item in itog_query:
        res_list.append(
            (item['product__name'], int(item['prod_count']))
        )

    return res_list


def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    f_start = Q(begin__gte=begin)
    f_end = Q(end__lte=end)

    f_start_date = Q(order__date_formation__gte=begin)
    f_end_date = Q(order__date_formation__lte=end)
    f_product = Q(product__name=product)

    order_item_query = OrderItem.objects.filter(f_start_date & f_end_date & f_product)

    f1 = Q(begin__lte=OuterRef("order__date_formation"))
    f2 = Q(end__gte=OuterRef("order__date_formation"))
    f3 = Q(product_id=OuterRef("product_id"))

    products_sudq1 = ProductCost.objects.filter(f_start & f_end).filter(f1 & f2 & f3)
    products_sudq_addit = ProductCost.objects.filter(f_start & f_end).filter(f3).order_by('-end')[:1]

    sum_q = (order_item_query.annotate(
        price=Subquery(products_sudq1.values('value'))
    ))

    sum_q0 = sum_q.annotate(
        all_pr=
        Case(
            When(price__isnull=True, then=Subquery(products_sudq_addit.values('value'))),
            default=F('price'), output_field=models.DecimalField()
        )
    ).annotate(
        summa=F('all_pr') * F('count'))

    query_all = sum_q0.values('order_id', 'order__number').annotate(all_sum=Sum(F('summa')))
    query_count_orders = query_all.aggregate(count_orders=Count(F('order_id')))
    query_all_sum = query_all.aggregate(sum_orders=Sum(F('all_sum')))

    if (int(query_count_orders['count_orders']) == 0):
        return 0
    else:
        return round(query_all_sum['sum_orders'] / query_count_orders['count_orders'], 0)