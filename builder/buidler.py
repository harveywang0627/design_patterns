from abc import ABC, abstractmethod


class Director(ABC):

    def __init__(self):
        self.__builder = None

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self.__builder.constructed_boject


class Builder(ABC):

    def __init__(self, constructed_object):
        self.constructed_object = constructed_object

    @abstractmethod
    def build_m_1(self):
        pass

    @abstractmethod
    def build_m_2(self):
        pass

    @abstractmethod
    def build_m_3(self):
        pass


class ConcreteBuilder(Builder):

    def build_m_1(self):
        pass

    def build_m_2(self):
        pass

    def build_m_3(self):
        pass


class ConcreteDirector(Director):

    def construct(self):
        self.__builder.build_m_1()
        self.__builder.build_m_2()
        self.__builder.build_m_3()

