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
