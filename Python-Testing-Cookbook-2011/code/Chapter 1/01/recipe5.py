class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val


import unittest


class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_parsing_millenia(self):
        self.assertEquals(1000, self.cvt.convert_to_decimal("M"))

    def test_parsing_century(self):
        self.assertEquals(100, self.cvt.convert_to_decimal("C"))


class RomanNumeralComboTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_multi_millenia(self):
        self.assertEquals(4000,self.cvt.convert_to_decimal("MMMM"))

    def test_multi_add_up(self):
        self.assertEquals(2010,self.cvt.convert_to_decimal("MMX"))
