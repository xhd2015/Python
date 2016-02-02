from planner.data import schedules, statuses, activities, schedule_error
from planner.persistence import file
from unittest import TestCase
from datetime import datetime, timedelta
from os import unlink

class test_system(TestCase):
    def setUp(self):
        self.A = statuses('A',
                          datetime.now(),
                          datetime.now() + timedelta(minutes = 7))
        self.B = statuses('B',
                          datetime.now() - timedelta(hours = 1),
                          datetime.now() + timedelta(hours = 1))
        self.C = statuses('C',
                          datetime.now() + timedelta(minutes = 10),
                          datetime.now() + timedelta(hours = 1))

        self.D = activities('D',
                            datetime.now(),
                            datetime.now() + timedelta(minutes = 7))

        self.E = activities('E',
                            datetime.now() + timedelta(minutes = 30),
                            datetime.now() + timedelta(hours = 1))

        self.F = activities('F',
                            datetime.now() - timedelta(minutes = 20),
                            datetime.now() + timedelta(minutes = 40))

    def tearDown(self):
        try:
            unlink('test_system.sqlite')
        except OSError:
            pass

    def test_usage_pattern(self):
        sched1 = schedules()

        sched1.add(self.A)
        sched1.add(self.B)
        sched1.add(self.C)
        sched1.add(self.D)
        sched1.add(self.E)

        store1 = file('test_system.sqlite')
        sched1.store(store1)

        del store1

        store2 = file('test_system.sqlite')
        sched2 = schedules.load(store2)

        self.assertEqual(sched1, sched2)

        sched2.remove(self.D)
        sched2.remove(self.E)

        self.assertNotEqual(sched1, sched2)

        sched2.add(self.F)

        self.assertTrue(self.F in sched2)
        self.assertFalse(self.F in sched1)

        self.assertRaises(schedule_error, sched2.add, self.D)
        self.assertRaises(schedule_error, sched2.add, self.E)

        self.assertTrue(self.A in sched1)
        self.assertTrue(self.B in sched1)
        self.assertTrue(self.C in sched1)
        self.assertTrue(self.D in sched1)
        self.assertTrue(self.E in sched1)
        self.assertFalse(self.F in sched1)

        self.assertTrue(self.A in sched2)
        self.assertTrue(self.B in sched2)
        self.assertTrue(self.C in sched2)
        self.assertFalse(self.D in sched2)
        self.assertFalse(self.E in sched2)
        self.assertTrue(self.F in sched2)
