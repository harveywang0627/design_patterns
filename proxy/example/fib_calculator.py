import time


class RawCalculator(object):

    def fib(self, n):
        if n < 2:
            return 1

        return self.fib(n - 2) + self.fib(n - 1)


def memoize(fn):

    __cache = {}

    def memoized(*args):

        key = (fn.__name__, args)
        if key in __cache:
            return __cache[key]
        __cache[key] = fn(*args)

        return __cache[key]

    return memoized


class CalculatorProxy(object):

    def __init__(self, target):
        self.target = target

        fib = getattr(self.target, "fib")
        setattr(self.target, "fib", memoize(fib))

    def __getattr__(self, item):
        return getattr(self.target, item)


if __name__ == "__main__":

    calculator = CalculatorProxy(RawCalculator())
    start_time = time.time()
    fib_sequence = [calculator.fib(x) for x in range(0, 80)]
    end_time = time.time()

    print("Calculating the list of {} Fibonacci numbers took {} seconds.".format(len(fib_sequence),
                                                                                 end_time - start_time))
