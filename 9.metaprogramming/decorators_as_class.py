# Good article
# http://www.ianbicking.org/blog/2008/10/decorators-and-descriptors.html

import types
from functools import wraps


class Profiled:

    def __init__(self, func):
        # dont understand this
        wraps(func)(self)
        self.ncalls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
        # return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        """
        This is only required for the situations when the decorator Profiled
        needs to be applied on class instances.
        Also, it is required because the invocation of class methods
        triggers the invocation of the __get__ method as part of the descriptor
        protocol
        """
        if instance is None:
            return self
        else:
            print("here....")
            return types.MethodType(self, instance)


# This is a function based implementation of the same wrapper
def profiler(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper


@Profiled
def add(a, b):
    return a + b


@profiler
def multiply(a, b):
    return a * b


class Spam:
    name = 'spam class'

    @Profiled
    def bar(self, x):
        print(self, x)

    @profiler
    def dab(self, x):
        print(self, x)
# add.ncalls

# add.ncalls should output the number of times the add
# function is called
