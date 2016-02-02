class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val

import unittest

class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        print "Creating a new RomanNumeralConverter..."
        self.cvt = RomanNumeralConverter()

    def tearDown(self):
        print "Destroying the RomanNumeralConverter..."
        self.cvt = None

    def test_parsing_millenia(self):
        self.assertEquals(1000, \
                          self.cvt.convert_to_decimal("M"))

    def test_parsing_century(self):
        self.assertEquals(100, \
                          self.cvt.convert_to_decimal("C"))

    def test_parsing_half_century(self):
        self.assertEquals(50, \
                          self.cvt.convert_to_decimal("L"))

    def test_parsing_decade(self):
        self.assertEquals(10, \
                          self.cvt.convert_to_decimal("X"))

    def test_parsing_half_decade(self):
        self.assertEquals(5, self.cvt.convert_to_decimal("V"))

    def test_parsing_one(self):
        self.assertEquals(1, self.cvt.convert_to_decimal("I"))

    def test_empty_roman_numeral(self):
        self.assertTrue(self.cvt.convert_to_decimal("") == 0)
        self.assertFalse(self.cvt.convert_to_decimal("") > 0)

    def test_no_roman_numeral(self):
        self.assertRaises(TypeError, \
                          self.cvt.convert_to_decimal, None)

if __name__ == "__main__":
    unittest.main()
