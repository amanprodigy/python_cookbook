# goal is to write a decorator that adds an optional argument
# to the function

# @timethis
# def add(a, b):
#     return a+b
# add(a, b, cache=True)

import time
from functools import wraps
from inspect import signature, Parameter


def timethis(func):
    results = dict()
    sig = signature(func)
    if 'cache' in sig.parameters:
        raise TypeError('{} already has {} as parameter'.format(
            func.__qualname__,
            'cache'
        ))

    @wraps(func)
    def wrapper(*args, cache=False, **kwargs):
        nonlocal results
        start = time.time()
        if cache is True:
            cached = results.get(args)
            if not cached:
                rv = func(*args, **kwargs)
                results[args] = rv
            else:
                rv = cached
        else:
            rv = func(*args, **kwargs)
            results[args] = rv
        end = time.time()
        seconds = end - start
        seconds = "{:10.9f}".format(seconds)
        print("Operation took %s seconds" % seconds)
        return rv
    parms = list(sig.parameters.values())
    parms.append(Parameter('debug',
                           Parameter.KEYWORD_ONLY,
                           default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


@timethis
def add(a, b):
    return a + b


@timethis
def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result
