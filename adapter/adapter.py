class ObjectAdapter(object):

    def __init__(self, what_i_have, provided_function):
        self.what_i_have = what_i_have
        self.required_function = provided_function

    def __getattr__(self, item):
        return getattr(self.what_i_have, item)
