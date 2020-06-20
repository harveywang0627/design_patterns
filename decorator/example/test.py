import unittest
import time
from decorator.example.time_decorator import time_calculate


class TestDecorator(unittest.TestCase):

    @staticmethod
    @time_calculate(unit="s")
    def time_sleep():
        time.sleep(2)

    def test_decorator(self):

        self.time_sleep()
