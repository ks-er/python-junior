from block_1.common import (
    MyException
)

class ClassFather:
    _name = 'Father-класс'
    registered_list = []

    @classmethod
    def register(cls):
        if cls._name != 'Father-класс' and issubclass(cls, ClassFather):
            cls.registered_list.append(cls._name)
        else:
            raise MyException

    @classmethod
    def get_name(cls):
        if issubclass(cls, ClassFather) and cls._name in cls.registered_list:
            return cls._name
        else:
            raise MyException

class User1(ClassFather):
    _name = 'User1'

class User2(ClassFather):
    _name = 'User2'
