import unittest
from adapter.example.computer_adapter import Computer, Human, Synthesizer, Adapter


class TestBuild(unittest.TestCase):

    def test_adapter(self):

        objects = [Computer('Asus')]
        synth = Synthesizer('moog')
        objects.append(Adapter(synth, dict(execute=synth.play)))
        human = Human('Bob')
        objects.append(Adapter(human, dict(execute=human.speak)))

        for i in objects:
            print('{} {}'.format(str(i), i.execute()))
            print('type is {}'.format(type(i)))
