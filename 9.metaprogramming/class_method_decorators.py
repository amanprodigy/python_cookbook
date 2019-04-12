from functools import wraps


class Student:

    def checkdivision(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            div, *_ = args
            if not isinstance(div, int):
                raise TypeError("{} must be of type {}".format(
                    div, int
                ))
            return func(*args, **kwargs)
        return wrapper

    def __int__(self, name, age):
        self._name = name
        self._age = age
        self._division = None


if __name__ == '__main__':
    s = Student()

    @s.checkdivision
    def set_division(div):
        print("Got division as {}".format(div))

    set_division(3)
    set_division('abc')
