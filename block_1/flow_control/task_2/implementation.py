def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """

    if to_scale == 'F':
        return 9/5 * value + 32
    elif to_scale == 'C':
        return 5/9 * (value - 32)
    else:
        return value
