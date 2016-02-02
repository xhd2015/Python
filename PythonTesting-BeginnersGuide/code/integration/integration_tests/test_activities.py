from unittest import TestCase
from planner.data import activities, task_error
from datetime import datetime

class activities_integration_tests(TestCase):
    def setUp(self):
        self.A = activities('A',
                          datetime(year = 2008, month = 7, day = 15),
                          datetime(year = 2009, month = 5, day = 2))

    def test_repr(self):
        self.assertEqual(repr(self.A), '<A 2008-07-15T00:00:00 2009-05-02T00:00:00>')

    def test_equality(self):
        self.assertEqual(self.A, self.A)
        self.assertNotEqual(self.A, activities('B',
                          datetime(year = 2008, month = 7, day = 15),
                          datetime(year = 2009, month = 5, day = 2)))
        self.assertNotEqual(self.A, activities('A',
                          datetime(year = 2007, month = 7, day = 15),
                          datetime(year = 2009, month = 5, day = 2)))
        self.assertNotEqual(self.A, activities('A',
                          datetime(year = 2008, month = 7, day = 15),
                          datetime(year = 2010, month = 5, day = 2)))

    def test_overlap_begin(self):
        activity = activities('activity name',
                          datetime(year = 2007, month = 8, day = 11),
                          datetime(year = 2008, month = 11, day = 27))

        self.assertTrue(activity.overlaps(self.A))
        self.assertTrue(activity.excludes(self.A))

    def test_overlap_end(self):
        activity = activities('activity name',
                          datetime(year = 2008, month = 1, day = 11),
                          datetime(year = 2010, month = 4, day = 16))

        self.assertTrue(activity.overlaps(self.A))
        self.assertTrue(activity.excludes(self.A))

    def test_overlap_inner(self):
        activity = activities('activity name',
                          datetime(year = 2007, month = 10, day = 11),
                          datetime(year = 2010, month = 1, day = 27))

        self.assertTrue(activity.overlaps(self.A))
        self.assertTrue(activity.excludes(self.A))

    def test_overlap_outer(self):
        activity = activities('activity name',
                          datetime(year = 2008, month = 8, day = 12),
                          datetime(year = 2008, month = 9, day = 15))

        self.assertTrue(activity.overlaps(self.A))
        self.assertTrue(activity.excludes(self.A))

    def test_overlap_after(self):
        activity = activities('activity name',
                          datetime(year = 2011, month = 2, day = 6),
                          datetime(year = 2015, month = 4, day = 27))

        self.assertFalse(activity.overlaps(self.A))


