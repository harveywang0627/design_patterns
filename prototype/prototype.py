from abc import ABC, abstractmethod
import copy


class ProtoType(ABC):

    @abstractmethod
    def show_properties(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class ObjectA(ProtoType):

    def __init__(self, a, b, c):
        self.property_a = a
        self.property_b = b
        self.property_c = c

    def show_properties(self):
        print("a")


class ObjectB(ProtoType):

    def __init__(self, e, f, g):
        self.property_e = e
        self.property_f = f
        self.property_g = g

    def show_properties(self):
        print("b")


class Builder(object):

    def __init__(self):

        self.map = {"A": ObjectA("a", "b", "c"),
                    "B": ObjectB("e", "f", "g")}

    def build(self, category):

        return self.map[category].clone()
