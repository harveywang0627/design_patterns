class RealObject(object):

    def __init__(self):
        self.p = ""

    def method1(self):
        pass

    def method2(self):
        pass


class ProxyObject(object):

    def __init__(self, target):
        self.target = target
        legacy_method = getattr(self.target, "method2")
        setattr(self.target, "method2", self.method2_wrap(legacy_method))

    @classmethod
    def method2_wrap(cls, f):

        def method2(*args, **kwargs):
            pass

        return method2

    def __getattr__(self, item):
        return getattr(self.target, item)
