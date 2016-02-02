from unittest import TestCase
from mocker import MockerTestCase, ANY
from planner.data import schedules, schedule_error
from datetime import datetime

class add_tests(MockerTestCase):
    def setUp(self):

        overlap_exclude = self.mocker.mock()
        overlap_exclude.overlaps(ANY)
        self.mocker.result(True)
        self.mocker.count(0, None)
        overlap_exclude.excludes(ANY)
        self.mocker.result(True)
        self.mocker.count(0, None)

        overlap_include = self.mocker.mock()
        overlap_include.overlaps(ANY)
        self.mocker.result(True)
        self.mocker.count(0, None)
        overlap_include.excludes(ANY)
        self.mocker.result(False)
        self.mocker.count(0, None)

        distinct_exclude = self.mocker.mock()
        distinct_exclude.overlaps(ANY)
        self.mocker.result(False)
        self.mocker.count(0, None)
        distinct_exclude.excludes(ANY)
        self.mocker.result(True)
        self.mocker.count(0, None)

        distinct_include = self.mocker.mock()
        distinct_include.overlaps(ANY)
        self.mocker.result(False)
        self.mocker.count(0, None)
        distinct_include.excludes(ANY)
        self.mocker.result(False)
        self.mocker.count(0, None)

        self.overlap_exclude = overlap_exclude
        self.overlap_include = overlap_include
        self.distinct_exclude = distinct_exclude
        self.distinct_include = distinct_include

        self.mocker.replay()

    def test_add_overlap_exclude(self):
        schedule = schedules()
        schedule.add(self.distinct_include)
        self.assertRaises(schedule_error,
                          schedule.add,
                          self.overlap_exclude)

    def test_add_overlap_include(self):
        schedule = schedules()
        schedule.add(self.distinct_include)
        schedule.add(self.overlap_include)

    def test_add_distinct_exclude(self):
        schedule = schedules()
        schedule.add(self.distinct_include)
        schedule.add(self.distinct_exclude)

    def test_add_distinct_include(self):
        schedule = schedules()
        schedule.add(self.distinct_include)
        schedule.add(self.distinct_include)

    def test_add_over_overlap_exclude(self):
        schedule = schedules()
        schedule.add(self.overlap_exclude)
        self.assertRaises(schedule_error,
                          schedule.add,
                          self.overlap_include)

    def test_add_over_distinct_exclude(self):
        schedule = schedules()
        schedule.add(self.distinct_exclude)
        self.assertRaises(schedule_error,
                          schedule.add,
                          self.overlap_include)

    def test_add_over_overlap_include(self):
        schedule = schedules()
        schedule.add(self.overlap_include)
        schedule.add(self.overlap_include)

    def test_add_over_distinct_include(self):
        schedule = schedules()
        schedule.add(self.distinct_include)
        schedule.add(self.overlap_include)

class in_tests(MockerTestCase):
    def setUp(self):
        fake = self.mocker.mock()
        fake.overlaps(ANY)
        self.mocker.result(True)
        self.mocker.count(0, None)
        fake.excludes(ANY)
        self.mocker.result(True)
        self.mocker.count(0, None)

        self.fake = fake

        self.mocker.replay()

    def test_in_before_add(self):
        schedule = schedules()
        self.assertFalse(self.fake in schedule)

    def test_in_after_add(self):
        schedule = schedules()
        schedule.add(self.fake)
        self.assertTrue(self.fake in schedule)
