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
