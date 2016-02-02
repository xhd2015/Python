from unittest import TestCase
from mocker import MockerTestCase
from planner.data import statuses, task_error
from datetime import datetime

class constructor_tests(TestCase):
    def test_valid(self):
        status = statuses('status name',
                          datetime(year = 2007, month = 9, day = 11),
                          datetime(year = 2008, month = 4, day = 27))

        self.assertEqual(status.name, 'status name')
        self.assertEqual(status.begins,
                         datetime(year = 2007, month = 9, day = 11))
        self.assertEqual(status.ends,
                         datetime(year = 2008, month = 4, day = 27))

    def test_backwards_times(self):
        self.assertRaises(task_error,
                          statuses,
                          'status name',
                          datetime(year = 2008, month = 4, day = 27),
                          datetime(year = 2007, month = 9, day = 11))

    def test_too_short(self):
        self.assertRaises(task_error,
                          statuses,
                          'status name',
                          datetime(year = 2008, month = 4, day = 27,
                                   hour = 7, minute = 15),
                          datetime(year = 2008, month = 4, day = 27,
                                   hour = 7, minute = 15))

class utility_tests(TestCase):
    def test_repr(self):
        status = statuses('status name',
                              datetime(year = 2007, month = 9, day = 11),
                              datetime(year = 2008, month = 4, day = 27))

        expected = "<status name 2007-09-11T00:00:00 2008-04-27T00:00:00>"

        self.assertEqual(repr(status), expected)

class exclusivity_tests(TestCase):
    def test_excludes(self):
        status = statuses('status name',
                          datetime(year = 2007, month = 9, day = 11),
                          datetime(year = 2007, month = 10, day = 6))

        # A status shouldn't exclude anything
        self.assertFalse(status.excludes(status))
        self.assertFalse(status.excludes(None))

class overlap_tests(MockerTestCase):
    def setUp(self):
        pseudo = self.mocker.mock()

        pseudo.begins
        self.mocker.result(datetime(year = 2007, month = 10, day = 7))
        self.mocker.count(1, None)

        pseudo.ends
        self.mocker.result(datetime(year = 2008, month = 2, day = 5))
        self.mocker.count(1, None)

        self.other = pseudo

        self.mocker.replay()

    def test_overlap_before(self):
        status = statuses('status name',
                          datetime(year = 2007, month = 9, day = 11),
                          datetime(year = 2007, month = 10, day = 6))

        self.assertFalse(status.overlaps(self.other))

    def test_overlap_begin(self):
        status = statuses('status name',
                          datetime(year = 2007, month = 8, day = 11),
                          datetime(year = 2007, month = 11, day = 27))

        self.assertTrue(status.overlaps(self.other))

    def test_overlap_end(self):
        status = statuses('status name',
                          datetime(year = 2008, month = 1, day = 11),
                          datetime(year = 2008, month = 4, day = 16))

        self.assertTrue(status.overlaps(self.other))

    def test_overlap_inner(self):
        status = statuses('status name',
                          datetime(year = 2007, month = 10, day = 11),
                          datetime(year = 2008, month = 1, day = 27))

        self.assertTrue(status.overlaps(self.other))

    def test_overlap_outer(self):
        status = statuses('status name',
                          datetime(year = 2007, month = 8, day = 12),
                          datetime(year = 2008, month = 3, day = 15))

        self.assertTrue(status.overlaps(self.other))

    def test_overlap_after(self):
        status = statuses('status name',
                          datetime(year = 2008, month = 2, day = 6),
                          datetime(year = 2008, month = 4, day = 27))

        self.assertFalse(status.overlaps(self.other))


