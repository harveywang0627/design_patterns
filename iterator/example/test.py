import unittest
from iterator.class_iterator import MyList


class TestIterator(unittest.TestCase):

    def test_iterator(self):
        my_list = MyList(1, 2, 3, 4, 5, 6)
        my_iterator = my_list.get_iterator()
        while my_iterator.has_next():
            print(my_iterator.next())
