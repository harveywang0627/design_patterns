import unittest
from command.example.calculator_command import AddCommand, SubCommand, Simulator, Invoker


class TestCommand(unittest.TestCase):

    def test_command(self):

        c = Simulator(10)

        invoker = Invoker()
        invoker.add_command(AddCommand(c, 10))
        invoker.add_command(SubCommand(c, 5))

        invoker.run()

        self.assertEqual(c.value, 15)

