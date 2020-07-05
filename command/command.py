class Command(object):

    def __init__(self, receiver, text):

        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.print_message(self.text)


class Receiver(object):

    def print_message(self, text):
        print("Message received : {}".format(text))


class Invoker(object):

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    receiver = Receiver()

    command1 = Command(receiver, "Execute command 1")
    command2 = Command(receiver, "Execute command 2")

    invoke = Invoker()
    invoke.add_command(command1)
    invoke.add_command(command2)

    invoke.run()
