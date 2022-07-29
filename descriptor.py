"""
    __get__(self, instance, owner):
        This method is called when you want to access the value of an attribute.
         This method takes two parameters by default.
          First instance, which refers to the object in which we are trying to call an attribute.
          Second, owner, which is the class to which the object belongs.

    __set__(self, instance, value):
        This method is called when you want to change the value of an attribute.
        This method takes two values by default.
        The first instance is the object whose attribute value you are going to change.
        The second value is the value you want to store in the attribute.

    __delete__(self, instance)):
        This method is called when we intend to remove an attribute from an object.
         This method needs only one parameter, which is the object whose attribute we are going to delete.

    __set_name__(self, owner, name):
        This method is used when you want to automatically name descriptor attributes.
        In this case, there is no need to send the value of the name after creating the class variable.
"""


class Descriptor:

    def __set_name__(self, owner, name):
        self.attribute_name = name  # name , car

    def __get__(self, instance, owner):
        return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be string.')
        instance.__dict__[self.attribute_name] = value

    def __delete__(self, instance):
        # del instance.__dict__[self.attribute_name]
        instance.__dict__[self.attribute_name] = None


class Person:
    name = Descriptor()  # name use in __set_name__
    car = Descriptor()  # car use in __set_name__

    def __init__(self, name, car):
        self.name = name
        self.car = car


person = Person('mohammadhssn', 'benz')
print(person.name)
print(person.car)

person.name = 'sara'
del person.car

print(person.name)  # sara
print(person.car)  # None
