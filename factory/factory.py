from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def make_object(self, name):
        pass


# -------------- simple factory ------------------------- #
class SQUARE(object):

    def __int__(self):

        self.x = 0
        self.y = 0


class CIRCLE(object):

    def __int__(self):
        self.d = 10


class ShapeFactory(AbstractFactory):

    @classmethod
    def make_object(cls, name):
        if name == "SQUARE":
            return SQUARE()
        elif name == "CIRCLE":
            return CIRCLE()
        else:
            return


# -------------- factory method -------------------------- #
class SquareFactory(AbstractFactory):

    def make_object(self, name):
        return SQUARE()


class CircleFactory(AbstractFactory):

    def make_object(self, name):
        return CIRCLE()


# ---------------- abstract factory ---------------------- #
class AbstractFactoryNew(ABC):

    @abstractmethod
    def produce_small(self):
        pass

    @abstractmethod
    def produce_large(self):
        pass


class SquareFactoryNew(AbstractFactoryNew):

    def produce_small(self):

        return SQUARE()

    def produce_large(self):
        return CIRCLE()


class CircleFactoryNew(AbstractFactoryNew):

    def produce_small(self):
        return CIRCLE()

    def produce_large(self):
        return CIRCLE()
