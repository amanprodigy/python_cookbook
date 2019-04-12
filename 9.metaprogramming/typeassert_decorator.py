from functools import wraps
from inspect import signature


def typeassert(*dargs, **dkwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func
        sig = signature(func)
        bound_types = sig.bind_partial(*dargs, **dkwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            # bind() is like bind_partial() except that
            # it does not allow for missing arguments
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError("Argument {} must be of type {}".format(
                            name, bound_types[name]
                        ))
            return func(*args, **kwargs)

        return wrapper
    return decorate


@typeassert(int, b=int, c=int)
def add(a, b, c):
    return a + b + c


print(add(2, 3, 5))
print(add(2, 'hello', 5))
print(add(2, 'hello', 'world'))
