import datetime
from functools import wraps


def time_calculate(unit="s"):

    def decorator(func):

        @wraps(func)
        def wrap(*args, **kwargs):
            st = datetime.datetime.utcnow()
            result = func(*args, **kwargs)
            et = datetime.datetime.utcnow()
            if unit == "s":
                print((et - st).total_seconds())
            return result
        return wrap

    return decorator
