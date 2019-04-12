from functools import wraps
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

def loggedv1(level, name=None, message=None):
    """
    Decorator to record logs based on user provided
    nam and message. If name is not provided the module
    will be used. If message is not provided the func
    name will be used
    """

    def decorator(func):
        """ This decorator will be used to collect the original
        function as its argument """

        # get the supplied logger name
        logname = name if name else func.__module__
        # instantiate a logger using the logger name
        logger = logging.getLogger(name=logname)
        # collect the log message
        logmessage = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            """ wrapper that executes the original
            function inside its control flow
            and utilizes the functions args """
            # log the message
            logger.log(level, msg=logmessage)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@loggedv1(logging.WARNING, 'Addition', 'Adding two numbers')
def add(a, b):
    return a+b


@loggedv1(logging.CRITICAL, 'Multiply', 'Multiplying two numbers')
def multiply(a, b):
    return a*b


class TestArgumentDecorator(unittest.TestCase):
    """ Basic Test Class """

    @loggedv1(logging.INFO, 'Testing addition')
    def test_addition(self):
        assert add(3, 4), 7

    @loggedv1(logging.INFO, 'Testing multiply')
    def test_multiplication(self):
        assert multiply(4, 5), 20


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
