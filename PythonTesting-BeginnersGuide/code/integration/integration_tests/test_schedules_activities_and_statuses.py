from planner.data import schedules, statuses, activities, schedule_error
from unittest import TestCase
from datetime import datetime, timedelta

class test_schedules_activities_and_statuses(TestCase):
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

    def test_usage_pattern(self):
        sched = schedules()

        sched.add(self.A)
        sched.add(self.B)
        sched.add(self.C)

        sched.add(self.D)

        self.assertTrue(self.A in sched)
        self.assertTrue(self.B in sched)
        self.assertTrue(self.C in sched)
        self.assertTrue(self.D in sched)

        self.assertRaises(schedule_error, sched.add, self.F)
        self.assertFalse(self.F in sched)

        sched.add(self.E)
        sched.remove(self.D)

        self.assertTrue(self.E in sched)
        self.assertFalse(self.D in sched)

        self.assertRaises(schedule_error, sched.add, self.F)

        self.assertFalse(self.F in sched)

        sched.remove(self.E)

        self.assertFalse(self.E in sched)

        sched.add(self.F)

        self.assertTrue(self.F in sched)
