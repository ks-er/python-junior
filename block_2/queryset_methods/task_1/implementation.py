def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    q_customer = Q(customer__name=name)
    query = Order.objects.all().select_related('customer', 'customer__name').filter(q_customer)

    return query.count()
