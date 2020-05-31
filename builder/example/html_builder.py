from abc import ABC, abstractmethod


class Director(ABC):

    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_obj(self):
        return self.builder.constructed_obj


class Builder(ABC):

    def __init__(self):
        self.constructed_obj = None

    @abstractmethod
    def add_text_field(self):
        pass

    @abstractmethod
    def add_button(self):
        pass

    @abstractmethod
    def add_checkbox(self):
        pass


class HtmlObject(object):

    def __init__(self):
        self.components = []


class HtmlPageBuilder(Builder):

    def __init__(self):
        super(HtmlPageBuilder, self).__init__()
        self.constructed_obj = HtmlObject()

    def add_text_field(self):
        self.constructed_obj.components.append("<br>abc</br>")

    def add_button(self):
        self.constructed_obj.components.append("<button>abc</button>")

    def add_checkbox(self):
        self.constructed_obj.components.append("<label>abc</label>")


class FormDirector(Director):

    def __init__(self):
        super(FormDirector, self).__init__()

    def construct(self):
        self.builder.add_text_field()
        self.builder.add_button()
        self.builder.add_checkbox()
