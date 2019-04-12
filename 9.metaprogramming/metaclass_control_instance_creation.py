import weakref


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance:
            return self.__instance
        else:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance


class Person(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


# Second example of caching instances using metaclass

class Cached(type):
    def __init__(self, *args, **kwargs):
        self.arg_to_instance_dict = weakref.WeakValueDictionary()
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if args in self.arg_to_instance_dict:
            return self.arg_to_instance_dict[args]
        else:
            obj = super().__call__(*args, **kwargs)
            self.arg_to_instance_dict[args] = obj
            return obj


class Student(metaclass=Cached):
    def __init__(self, name):
        print('Initiating student with name %s' % name)
        self.name = name


if __name__ == '__main__':
    p1 = Person('Aman')
    p1.name
    # >> Aman
    p2 = Person('Richa')
    p2.name
    # >> Aman
    p1 is p2
    # >> True

    s = Student('Aman')
    # >> Initiating student with name Aman

    s1 = Student('Richa')
    # >> Initiating student with name Richa

    s1.name
    # Out[3]: 'Richa'

    s.name
    # Out[4]: 'Aman'

    s2 = Student('Aman')

    s2 is s1
    # Out[6]: False
