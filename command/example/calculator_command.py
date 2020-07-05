class AddCommand(object):

    def __init__(self, receiver, value):

        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.add(self.value)


class SubCommand(object):

    def __init__(self, receiver, value):

        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.subtract(self.value)


class Simulator(object):

    def __init__(self, value):

        self.value = value

    def add(self, num):
        self.value += num

    def subtract(self, num):
        self.value -= num


class Invoker(object):

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()

