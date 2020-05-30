import unittest
from singleton.example.global_logger import GlobalLogger


class TestLogger(unittest.TestCase):

    def test_logger(self):

        obj1 = GlobalLogger("Test1", "DEBUG")
        obj2 = GlobalLogger("Test2", "DEBUG")
        logger1 = obj1.get_logger()
        logger2 = obj2.get_logger()

        logger1.info("This is logger 1 info output.")
        logger2.warning("This is logger 2 warning output.")

        self.assertEqual(obj1.logger_name, obj2.logger_name)
