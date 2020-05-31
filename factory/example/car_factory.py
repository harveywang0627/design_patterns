from abc import ABC,abstractmethod


class AbstractCarFactory(ABC):

    @abstractmethod
    def produce_a_car(self):
        pass

    @abstractmethod
    def produce_b_car(self):
        pass


class CarBMW(object):

    def __init__(self, level):
        self.level = level
        self.name = "BMW"


class CarAudi(object):

    def __init__(self, level):
        self.level = level
        self.name = "Audit"


class BMWCarFactory(AbstractCarFactory):

    def produce_a_car(self):
        return CarBMW("A")

    def produce_b_car(self):
        return CarBMW("B")


class AudiFactory(AbstractCarFactory):

    def produce_a_car(self):
        return CarAudi("A")

    def produce_b_car(self):
        return CarAudi("B")
