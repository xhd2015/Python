def convert_to_basen(value, base):
    """Convert a base10 number to basen.

    >>> [convert_to_basen(i, 16) for i in range(1,16)] #doctest: +NORMALIZE_WHITESPACE
    ['1/16', '2/16', '3/16', '4/16', '5/16', '6/16', '7/16', '8/16', 
    '9/16',  'a/16', 'b/16', 'c/16', 'd/16', 'e/16', 'f/16']

    FUTURE: Binary may support 2's complement in the future, but not now.
    >>> convert_to_basen(-10, 2) #doctest: +SKIP
    '0110/2'

    BUG: Discovered that this algorithm doesn't handle 0. Need to patch it.
    TODO: Renable this when patched.
    >>> convert_to_basen(0, 2) #doctest: +SKIP
    '0/2'
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
