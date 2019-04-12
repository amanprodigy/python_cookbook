import random
from weakref import WeakKeyDictionary


# This is a correct implementation as the instance of farenheit is being
# used to get and set the value of the celcius property inside the Farenheit
# class
class Celcius:

    def __get__(self, instance, owner):
        return 5 * (instance.farenheit - 32) / 9

    def __set__(self, instance, value):
        instance.farenheit = 32 + 9 * value / 5


class Farenheit:
    celcius = Celcius()

    def __init__(self, initial_f):
        self.farenheit = initial_f


# Following is descriptor #2
# this is a rather incorrect implementation since qty on product
# instances will always be same since quantity is being set at the
# class level of quantity
# We shoud use a wekref dictionary so that the Descriptor class
# rejects the last dictionary of the name, value pair of the property
class Quantity(object):
    _value = 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("{} must be of type {}".format(
                'qty',
                int
            ))
        self._value = value


class Product(object):
    price = Quantity()

    def __init__(self, name, price):
        self.name = name
        self.price = price


# This descriptor is also wrongly implemented for the same reason as above
class Price1(object):
    def __init__(self):
        self.__price = 0

    def __get__(self, instance, owner):
        return self.__price

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.__price = value

    def __delete__(self, instance):
        del self.__price

    def somefunction(self):
        print('hello')
# >>> b1 = Book("William Faulkner", "The Sound and the Fury", 12)
# >>> b1.price
# 12
# >>> b2 = Book("John Dos Passos", "Manhattan Transfer", 13)
# >>> b1.price
# 13


# Following is a correct implementation using the weakref
# https://www.smallsurething.com/python-descriptors-made-simple/
class Price2(object):
    def __init__(self):
        self.default = 0
        self.values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.values.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.values[instance] = value

    def __delete__(self, instance):
        del self.values[instance]


class Book(object):
    price = Price2()

    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def __str__(self):
        return "{0} - {1}".format(self.author, self.title)
# >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
# >>> b.price
# 12
# >>> b.price = -12
# Traceback (most recent call last):
#   File "<pyshell#68>", line 1, in <module>
#     b.price = -12
#   File "<pyshell#58>", line 9, in __set__
#     raise ValueError("Price must be between 0 and 100.")
# ValueError: Price must be between 0 and 100.
# >>> b.price = 101
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     b.price = 101
#   File "<pyshell#58>", line 9, in __set__
#     raise ValueError("Price must be between 0 and 100.")
# ValueError: Price must be between 0 and 100.


# Another example of a descriptor
class Die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def __get__(self, instance, owner):
        return int(random.random() * self.sides) + 1


class Game(object):
    d6 = Die()
    d10 = Die(sides=10)
    d20 = Die(sides=20)


# Creating descriptors using property of python
# https://developer.ibm.com/tutorials/os-pythondescriptors/
class Student(object):

    def init(self):
        self._name = ''

    @property
    def name(self):
        print("Getting: %s" % self._name)
        return self._name

    @name.setter
    def name(self, value):
        print("Setting: %s" % value)
        self._name = value.title()

    @name.deleter
    def name(self):
        print(">Deleting: %s" % self._name)
        del self._name


# Another way of writing descriptor using property
class Publisher(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print("getting name")
        return self.__name

    def set_name(self, value):
        print("setting name")
        self.__name = value

    def delete_name(self):
        print("deleting name")
        del self.__name

    name = property(get_name, set_name, delete_name, "Publisher name")

# Another interesting read. Combining the realm of
# decorators and descriptors
# http://www.ianbicking.org/blog/2008/10/decorators-and-descriptors.html


if __name__ == '__main__':
    f = Farenheit(100)
    f.celcius   # prints 37.77
    f.celcius = 20
    f.celcius   # prints 20.0

    p1 = Product('Bat', 21)
    p1.price
    p2 = Product('Ball', 11)

    Game.d6
    Game.d10
    Game.d20
    game = Game()
    game.d20
