import unittest
from recipe8 import *

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_to_decimal1(self):
        self.assertEquals(0, self.cvt.convert_to_decimal(""))

    def test_to_decimal2(self):
        self.assertEquals(1, self.cvt.convert_to_decimal("I"))

    def test_to_decimal3(self):
        self.assertEquals(2010, \
                          self.cvt.convert_to_decimal("MMX"))

    def test_to_decimal4(self):
        self.assertEquals(4000, \
                          self.cvt.convert_to_decimal("MMMM"))

    def test_convert_to_roman1(self):
        self.assertEquals("", self.cvt.convert_to_roman(0))

    def test_convert_to_roman2(self):
        self.assertEquals("II", self.cvt.convert_to_roman(2))

    def test_convert_to_roman3(self):
        self.assertEquals("V", self.cvt.convert_to_roman(5))

    def test_convert_to_roman4(self):
        self.assertEquals("XII", \
                          self.cvt.convert_to_roman(12))

    def test_convert_to_roman5(self):
        self.assertEquals("MMX", \
                          self.cvt.convert_to_roman(2010))

    def test_convert_to_roman6(self):
        self.assertEquals("MMMM", \
                          self.cvt.convert_to_roman(4000))

if __name__ == "__main__":
    unittest.main()

