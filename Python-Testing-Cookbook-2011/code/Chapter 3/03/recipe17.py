def convert_to_basen(value, base):
    """Convert a base10 number to basen.

    >>> convert_to_basen(0, 2)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    >>> convert_to_basen(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
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
