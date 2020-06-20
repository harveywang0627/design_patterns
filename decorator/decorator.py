from functools import wraps


def decorators_parameters(a):

    def decorators(func):

        @wraps(func)
        def wrap(*args, **kwargs):

            return func(*args, **kwargs)

        return wrap

    return decorators







