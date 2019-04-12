from functools import wraps, partial
import logging
import unittest

"""
@decorator(x, y, z)
def func(a, b):
    pass

is equivalent to

def func(a, b):
    pass
func = decorator(x, y, z)(func)
"""


def attach_to_wrapper(obj, func=None):
    if func is None:
        return partial(attach_to_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def loggedv2(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        logger = logging.getLogger(name=logname)
        logmessage = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, msg=logmessage)
            return func(*args, **kwargs)

        @attach_to_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_to_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmessage
            logmessage = newmsg

        @attach_to_wrapper(wrapper)
        def get_level():
            return level

        @attach_to_wrapper(wrapper)
        def get_message():
            return message

        return wrapper
    return decorate


@loggedv2(logging.INFO, 'add', 'Addition')
def add(a, b):
    return a+b


@loggedv2(logging.INFO, 'multiply', 'Multiplication')
def multiply(a, b):
    return a*b


class TestAccessorDecorator(unittest.TestCase):

    @loggedv2(logging.DEBUG, 'Testing addition')
    def test_addition(self):
        add(2, 3)
        add.set_level(logging.WARNING)
        add(4, 5)
        assert multiply.get_level(), logging.WARNING

    @loggedv2(logging.DEBUG, 'Testing multiply')
    def test_multiplication(self):
        multiply(2, 3)
        multiply.set_message('Multiply called')
        multiply(4, 5)
        assert multiply.get_message(), 'Multiply called'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
