import unittest
from builder.example.html_builder import FormDirector, HtmlPageBuilder


class TestBuild(unittest.TestCase):

    def test_builder(self):

        bl = HtmlPageBuilder()
        fd = FormDirector()
        fd.set_builder(bl)
        fd.construct()
        result = fd.get_constructed_obj()

        self.assertEqual(len(result.components), 3)
