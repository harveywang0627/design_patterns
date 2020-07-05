import unittest
from responsibility.example.chain_of_print import Handler1, Handler2, main_handler


class TestChain(unittest.TestCase):

    def test_chain(self):

        hd = Handler1()
        hd.next_handler = Handler2()

        request = {"test": "a"}

        main_handler(hd, request)
