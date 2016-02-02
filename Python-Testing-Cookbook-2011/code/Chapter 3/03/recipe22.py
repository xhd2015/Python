def convert_to_basen(value, base):
    """Convert a base10 number to basen.

    These show the edges for base 2.
    >>> convert_to_basen(1, 2)
    '1/2'
    >>> convert_to_basen(2, 2)
    '10/2'
    >>> convert_to_basen(0, 2)
    Traceback (most recent call last):
       ...
    ValueError: math domain error

    These show the edges for base 36.
    >>> convert_to_basen(1, 36)
    '1/36'
    >>> convert_to_basen(35, 36)
    'z/36'
    >>> convert_to_basen(36, 36)
    '10/36'
    >>> convert_to_basen(0, 36)
    Traceback (most recent call last):
       ...
    ValueError: math domain error

    These show the edges for base 37.
    >>> convert_to_basen(1, 37)
    Traceback (most recent call last):
       ...
    Exception: Only support bases 2-36
    >>> convert_to_basen(36, 37)
    Traceback (most recent call last):
       ...
    Exception: Only support bases 2-36
    >>> convert_to_basen(37, 37)
    Traceback (most recent call last):
       ...
    Exception: Only support bases 2-36
    >>> convert_to_basen(0, 37)    
    Traceback (most recent call last):
       ...
    Exception: Only support bases 2-36
    """
    if base < 2 or base > 36:
        raise Exception("Only support bases 2-36")

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
