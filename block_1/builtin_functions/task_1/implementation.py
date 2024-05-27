from block_1.common import (
    MyException
)

class Value:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        try:
            result = self.value + other
        except:
            raise MyException
        else:
            return result
         

    def __sub__(self, other):
        try:
            result = self.value - other
        except:
            raise MyException
        else:
            return result
    
    def __mul__(self, other):
        try:
            result = self.value * other
        except:
            raise MyException
        else:
            return result
    
    def __truediv__(self, other):
        try:
            result = self.value / other        
        except:
            raise MyException
        else:
            return result
