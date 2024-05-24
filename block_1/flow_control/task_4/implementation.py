from datetime import (
    timedelta
)

def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    
    return some_date + timedelta(days=1)
