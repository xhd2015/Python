class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val

    def convert_to_roman(self, decimal):
        val = ""
        while decimal > 1000:
            val += "M"
            decimal -= 1000
        while decimal > 500:
            val += "D"
            decimal -= 500
        while decimal > 100:
            val += "C"
            decimal -= 100
        while decimal > 50:
            val += "L"
            decimal -= 50
        while decimal > 10:
            val += "X"
            decimal -= 10
        while decimal > 5:
            val += "V"
            decimal -= 5
        while decimal > 1:
            val += "I"
            decimal -= 1
        return val

