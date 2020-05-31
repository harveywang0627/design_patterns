import unittest
from factory.example.car_factory import BMWCarFactory, AudiFactory


class TestFactory(unittest.TestCase):

    def test_factory(self):

        bmw_a_car = BMWCarFactory().produce_a_car()
        audi_b_car = AudiFactory().produce_b_car()
        self.assertEqual(bmw_a_car.name, "BMW")
        self.assertEqual(audi_b_car.level, "B")
