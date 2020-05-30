import unittest
from prototype.example.ResumePrinter import ResumePrinter
from prototype.example.ResumePrinter import SoftWareResume
import datetime


class TestProto(unittest.TestCase):

    def test_proto(self):
        resumes = []
        st = datetime.datetime.now().timestamp()*1000
        rp = ResumePrinter()
        for i in range(0, 5000):
            resumes.append(rp.get_resume("SOFTWARE"))
        et = datetime.datetime.now().timestamp() * 1000
        time_1 = et - st

        st = datetime.datetime.now().timestamp() * 1000
        for i in range(0, 5000):
            resumes.append(SoftWareResume("Jack", "1991", "100"))
        et = datetime.datetime.now().timestamp() * 1000

        time_2 = et - st

        self.assertTrue(time_1 < time_2)
