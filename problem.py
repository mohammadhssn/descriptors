"""
    property, getter, setter, deleter

    The problem of not using descriptors:
        The problem is that when the number of attributes increases, we end up with repetitive code to manage them
"""


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be string.')
        self._name = value

    @name.deleter
    def name(self):
        self._name = None

    # -------------------------

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('Value must be integer.')
        self._age = value

    @age.deleter
    def age(self):
        del self._age


person = Person('mohammadhssn', 23)

person.name = 'sara'  # sara
print(person.name)

del person.name  # None
print(person.name)
