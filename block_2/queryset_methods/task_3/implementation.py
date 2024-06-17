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
