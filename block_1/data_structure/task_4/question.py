"""
Может ли кортеж, содержащий список, быть ключом словаря? Почему?
"""

"""
Ответ:
Есть общее правило:
только неизменяемый (immutable) тип данных можно использовать как ключ в словаре.

В теории, кортеж неизменяемый, однако он содержит список,который является изменяемым.
Если кортеж содержит любой изменяемый объект прямо или косвенно, 
он не может использоваться в качестве ключа. Поэтому кортеж, содержащий список, ключом словаря быть НЕ МОЖЕТ.

Однако это можно обойти.
Цитата из документации:
>>>>>
Проблема в том, что не только объект верхнего уровня может изменить свое значение; 
вы можете использовать кортеж, содержащий список, в качестве ключа.
Ввод чего-либо в качестве ключа в словарь потребует пометки всех объектов, доступных оттуда, 
как доступных только для чтения.
Если вам нужно, есть способ обойти это, но используйте его на свой страх и риск: 
вы можете обернуть изменяемую структуру внутри экземпляра класса, который имеет как метод, 
так __eq__()и __hash__()метод.
Затем вы должны убедиться, что хеш-значение для всех таких объектов-оболочек, 
которые находятся в словаре (или другой хэш-структуре), остается фиксированным, 
пока объект находится в словаре (или другой структуре)
"""
