import unittest
from recipe1 import RomanNumeralConverter


class BadTest(unittest.TestCase):
    def test_no_roman_numeral(self):
        value = RomanNumeralConverter(None)
        try:
            value.convert_to_decimal()
            self.fail("Expected a TypeError")
        except TypeError as e:
            pass
