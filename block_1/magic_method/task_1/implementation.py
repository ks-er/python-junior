import math

from common import (
    MyException
)

class Multiplier:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        try:
            result = Multiplier(self.value + obj.value)
        except:
            raise MyException
        else:
            return result
    
    def __iadd__(self, obj):
        try:
            result = Multiplier(self.value + obj.value)
        except:
            raise MyException
        else:
            return result

    def __sub__(self, obj):
        try:
            result = Multiplier(self.value - obj.value)
        except:
            raise MyException
        else:
            return result
        
    def __isub__(self, obj):
        try:
            result = Multiplier(self.value - obj.value)
        except:
            raise MyException
        else:
            return result
    
    def __mul__(self, obj):
        try:
            result = Multiplier(self.value * obj.value)
        except:
            raise MyException
        else:
            return result
    
    def __imul__(self, obj):
        try:
            result = Multiplier(self.value * obj.value)
        except:
            raise MyException
        else:
            return result
    
    def __truediv__(self, obj):
        try:
            result = Multiplier(self.value / obj.value)
        except:
            raise MyException
        else:
            return result
    
    def __itruediv__(self, obj):
        try:
            result = Multiplier(self.value / obj.value)
        except:
            raise MyException
        else:
            return result

    def get_value(self):
        return math.trunc(self.value)


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.value = value * 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.value = value * 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.value = value * 1000000
