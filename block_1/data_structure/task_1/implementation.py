class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    values = ()

    def __init__(self, *args):
        self.values = args

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        valueList = [item for item in self.values if item == value]
        return len(valueList)

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        if (value not in self.values):
            raise ValueError
        else:
            for index in range(0, len(self.values)):
                if self.values[index] == value:
                     return index
                else:
                    continue
                    
        raise NotImplementedError

    def __getitem__(self, key):
        if len(self.values) >= key:
            return self.values[key]
        else:
            raise ValueError
