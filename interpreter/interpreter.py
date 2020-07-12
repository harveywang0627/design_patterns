class NonTerminal(object):

    def __int__(self, expression):
        self.expression = expression

    def interpret(self):
        self.expression.interpret()


class Terminal(object):
    def interpret(self):
        pass
