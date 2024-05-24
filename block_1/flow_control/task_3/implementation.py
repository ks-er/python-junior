from datetime import (
    datetime
)

def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """

    months = {
        'январь':31,
        'февраль': getFebriaryDays(),
        'март':31,
        'апрель':30,
        'май':31,
        'июнь':30,
        'июль':31,
        'август':31,
        'сентябрь':30,
        'октябрь':31,
        'ноябрь':30,
        'декабрь':31
    }

    if month in months.keys():
        return months[month]
    else:
        return 0

def getFebriaryDays():
    year = datetime.now().year
    if year % 4 == 0: 
        return 29 
    else: return 28
