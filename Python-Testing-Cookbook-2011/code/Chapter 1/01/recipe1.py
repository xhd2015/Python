class RomanNumeralConverter(object):
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.digit_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def convert_to_decimal(self):
        val = 0
        for char in self.roman_numeral:
            val += self.digit_map[char]
        return val


import unittest


class RomanNumeralConverterTest(unittest.TestCase):
    def test_parsing_millenia(self):
        value = RomanNumeralConverter("M")
        self.assertEquals(1000, value.convert_to_decimal())

    def test_parsing_century(self):
        value = RomanNumeralConverter("C")
        self.assertEquals(100, value.convert_to_decimal())

    def test_parsing_half_century(self):
        value = RomanNumeralConverter("L")
        self.assertEquals(50, value.convert_to_decimal())

    def test_parsing_decade(self):
        value = RomanNumeralConverter("X")
        self.assertEquals(10, value.convert_to_decimal())

    def test_parsing_half_decade(self):
        value = RomanNumeralConverter("V")
        self.assertEquals(5, value.convert_to_decimal())

    def test_parsing_one(self):
        value = RomanNumeralConverter("I")
        self.assertEquals(1, value.convert_to_decimal())

    def test_empty_roman_numeral(self):
        value = RomanNumeralConverter("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)

    def test_no_roman_numeral(self):
        value = RomanNumeralConverter(None)
        self.assertRaises(TypeError, value.convert_to_decimal)


if __name__ == "__main__":
    unittest.main()
