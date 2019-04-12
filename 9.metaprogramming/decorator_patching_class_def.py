def logger(cls):
    orig_attr = cls.__getattribute__

    def new_getattribute(self, x):
        print('logging here')
        return orig_attr(self, x)

    cls.__getattribute__ = new_getattribute

    return cls


@logger
class Student:
    age = None

    def __init__(self, name):
        self.name = name

    def getage(self):
        return self.age

    def setage(self, a):
        self.age = a


# Following is an implementation using inheritance and super()
# achieving same result
class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)


# Example:
class A(LoggedGetattribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass
