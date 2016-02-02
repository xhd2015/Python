def convert_to_basen(value, base):
    """Convert a base10 number to basen.

    >>> convert_to_basen(1, 2)
    '1/2'
    >>> convert_to_basen(2, 2)
    '10/2'
    >>> convert_to_basen(3, 2)
    '11/2'
    >>> convert_to_basen(4, 2)
    '100/2'
    >>> convert_to_basen(5, 2)
    '101/2'
    >>> convert_to_basen(6, 2)
    '110/2'
    >>> convert_to_basen(7, 2)
    '111/2'
    >>> convert_to_basen(1, 16)
    '1/16'
    >>> convert_to_basen(10, 16)
    'a/16'
    >>> convert_to_basen(15, 16)
    'f/16'
    >>> convert_to_basen(16, 16)
    '10/16'
    >>> convert_to_basen(31, 16)
    '1f/16'
    >>> convert_to_basen(32, 16)
    '20/16'
    """
    
    import math

    def _convert(remaining_value, base, exp):
        def stringify(value):
            if value > 9:
                return chr(value + ord('a')-10)
            else:
                return str(value)

        if remaining_value >= 0 and exp >= 0:
            factor = int(math.pow(base, exp))
            if factor <= remaining_value:
                multiple = remaining_value / factor
                return stringify(multiple) + \
                  _convert(remaining_value-multiple*factor, \
                                base, exp-1)
            else:
                return "0" + \
                       _convert(remaining_value, base, exp-1)
        else:
            return ""

    return "%s/%s" % (_convert(value, base, \
                         int(math.log(value, base))), base)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
