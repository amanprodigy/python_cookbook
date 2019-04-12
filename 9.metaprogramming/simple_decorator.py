from functools import wraps
import time
import unittest

"""
@deco
def func(x, y):
    pass

--- is equivalent to ---

def func(x, y):
    pass
deco = deco(func)
"""

def timeit(func):
    """ Simple decorator to record time of an operation """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Operation took {} seconds".format(end-start))
    return wrapper


@timeit
def add(a, b):
    """ function to add two numbers """
    return a + b


@timeit
def countdown(n):
    """ function to countdown from given number to 0 """
    if n > 0:
        n -= 1


class TestSimpleDecorator(unittest.TestCase):
    """ Basic Test Class """

    def test_timeit(self):
        add(3, 4)
        countdown(300000)

        print(countdown.__name__)
        print(countdown.__doc__)
        print(countdown.__wrapped__)

        # decorator not invoked. Original function called"""
        countdown.__wrapped__(100000)


if __name__ == '__main__':
    unittest.main()
