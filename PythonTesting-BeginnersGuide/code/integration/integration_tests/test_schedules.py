from unittest import TestCase
from mocker import MockerTestCase, MATCH, ANY
from planner.data import schedules, schedule_error
from datetime import datetime

class schedules_tests(MockerTestCase):
    def setUp(self):
        mocker = self.mocker

        A = mocker.mock()
        A.__eq__(MATCH(lambda x: x is A))
        mocker.result(True)
        mocker.count(0, None)
        A.__eq__(MATCH(lambda x: x is not A))
        mocker.result(False)
        mocker.count(0, None)
        A.overlaps(ANY)
        mocker.result(False)
        mocker.count(0, None)
        A.begins
        mocker.result(5)
        mocker.count(0, None)

        B = mocker.mock()
        A.__eq__(MATCH(lambda x: x is B))
        mocker.result(True)
        mocker.count(0, None)
        B.__eq__(MATCH(lambda x: x is not B))
        mocker.result(False)
        mocker.count(0, None)
        B.overlaps(ANY)
        mocker.result(False)
        mocker.count(0, None)
        B.begins
        mocker.result(3)
        mocker.count(0, None)

        C = mocker.mock()
        C.__eq__(MATCH(lambda x: x is C))
        mocker.result(True)
        mocker.count(0, None)
        C.__eq__(MATCH(lambda x: x is not C))
        mocker.result(False)
        mocker.count(0, None)
        C.overlaps(ANY)
        mocker.result(False)
        mocker.count(0, None)
        C.begins
        mocker.result(7)
        mocker.count(0, None)

        self.A = A
        self.B = B
        self.C = C

        mocker.replay()

    def test_equality(self):
        sched1 = schedules()
        sched2 = schedules()

        self.assertEqual(sched1, sched2)

        sched1.add(self.A)
        sched1.add(self.B)

        sched2.add(self.A)
        sched2.add(self.B)
        sched2.add(self.C)

        self.assertNotEqual(sched1, sched2)

        sched1.add(self.C)

        self.assertEqual(sched1, sched2)
