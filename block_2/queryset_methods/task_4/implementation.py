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
