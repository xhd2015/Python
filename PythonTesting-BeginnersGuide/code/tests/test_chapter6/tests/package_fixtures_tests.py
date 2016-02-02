from unittest import TestCase
from datetime import datetime

class first_tests(TestCase):
    def test_year(self):
        self.assertEqual(datetime.now().year, 2009)

    def test_month(self):
        self.assertEqual(datetime.now().month, 6)

    def test_day(self):
        self.assertEqual(datetime.now().day, 12)

    def test_hour(self):
        self.assertEqual(datetime.now().hour, 10)

    def test_minute(self):
        self.assertEqual(datetime.now().minute, 15)

    def test_second(self):
        self.assertEqual(datetime.now().second, 5)

