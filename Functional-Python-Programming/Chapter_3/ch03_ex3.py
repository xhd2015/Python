#!/usr/bin/env python3
"""Functional Python Programming

Chapter 3, Example Set ?
"""

def strip_head( source, line ):
    """Purely recursive strip headings until a blank line.

    >>> import io
    >>> data = io.StringIO( "heading\\n\\nbody\\nmore\\n" )
    >>> tail, first = strip_head(data,data.readline())
    >>> first
    'body\\n'
    >>> list(tail)
    ['more\\n']

    """
    if len(line.strip()) == 0:
        return source, source.readline()
    return strip_head( source, source.readline() )

def get_columns( source, line ):
    """When reading 1000.txt, parse columns and exclude the trailing line.

    >>> import io
    >>> data = io.StringIO( "body\\nmore\\nend.\\n" )
    >>> list( get_columns(data, data.readline() ) )
    ['body\\n', 'more\\n']
    """
    if line.strip() == "end.": return
    yield line
    yield from get_columns( source, source.readline() )
    #for data in get_columns( source, source.readline() ):
    #    yield data

def parse_i( source ):
    """Imperative parsing.

    >>> import io
    >>> data = io.StringIO('''\\
    ...                         The First 1,000 Primes
    ...                          (the 1,000th is 7919)
    ...         For more information on primes see http://primes.utm.edu/
    ...
    ...      2      3      5      7     11     13     17     19     23     29
    ...   7841   7853   7867   7873   7877   7879   7883   7901   7907   7919
    ... end.
    ... ''')
    >>> list( parse_i(data))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919]
    """
    for c in get_columns( *strip_head( source, source.readline() ) ):
        for number_text in c.split():
            yield int(number_text)

def parse_g( source ):
    """Generator function parsing.

    >>> import io
    >>> data = io.StringIO('''\\
    ...                         The First 1,000 Primes
    ...                          (the 1,000th is 7919)
    ...         For more information on primes see http://primes.utm.edu/
    ...
    ...      2      3      5      7     11     13     17     19     23     29
    ...   7841   7853   7867   7873   7877   7879   7883   7901   7907   7919
    ... end.
    ... ''')
    >>> list( parse_g(data))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919]
    """
    return ( int(number_text)
            for c in get_columns( *strip_head( source, source.readline() ) )
                for number_text in c.split()
        )

def performance():
    with open("1000.txt") as source:
        primes= list(parse_g(source))
    assert len(primes) == 1000

    from Chapter_2.ch02_ex1 import isprimei # Faster than isprimer, isprimeg

    import time

    start= time.perf_counter()
    for repeat in range(1000):
        assert all( isprimei(x) for x in primes )
    print( time.perf_counter() - start )

    start= time.perf_counter()
    for repeat in range(1000):
        assert not any( not isprimei(x) for x in primes )
    print( time.perf_counter() - start )

    from functools import reduce
    start= time.perf_counter()
    for repeat in range(1000):
        assert reduce( lambda x,y : x and y, (isprimei(x) for x in primes) )
    print( time.perf_counter() - start )

def group_by_seq( n, sequence ):
    flat_iter=iter(sequence)
    full_sized_items = list( tuple(next(flat_iter)
        for i in range(n))
            for row in range(len(sequence)//n))
    trailer = tuple(flat_iter)
    if trailer:
        return full_sized_items + [trailer]
    else:
        return full_sized_items

def group_by_iter( n, iterable ):
    row= tuple(next(iterable) for i in range(n))
    while row:
        yield row
        row= tuple(next(iterable) for i in range(n))

from itertools import zip_longest
def group_by_slice( n, sequence ):
    return zip_longest( *(sequence[i::n] for i in range(n)) )

parser_test= """
>>> text= '''   2      3      5      7     11     13     17     19     23     29
...  31     37     41     43     47     53     59     61     67     71
... 179    181    191    193    197    199    211    223    227    229
... '''
>>> data= list(v for line in text.splitlines() for v in line.split())
>>> data
['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '179', '181', '191', '193', '197', '199', '211', '223', '227', '229']

"""

grouping_test= """
>>> with open("1000.txt") as source:
...     flat= list(parse_g(source))
>>> len(flat)
1000

>>> group7_seq= group_by_seq( 7, flat )
>>> group7_seq[-1]
(7877, 7879, 7883, 7901, 7907, 7919)

>>> demo= list(x for line in group7_seq for x in line)
>>> demo == flat
True

>>> group7_iter= list(group_by_iter( 7, iter(flat) ))

>>> group7_iter[-1]
(7877, 7879, 7883, 7901, 7907, 7919)

>>> demo= list(x for line in group7_iter for x in line)
>>> demo == flat
True

>>> all= list(group_by_slice( 7, flat ))
>>> all[0]
(2, 3, 5, 7, 11, 13, 17)
>>> all[-1]
(7877, 7879, 7883, 7901, 7907, 7919, None)
"""

__test__ = {
    "parser_test": parser_test,
    "grouping_test": grouping_test
}

def digits( x, b ):
    """Digits in  given base.

    >>> tuple(digits(126, 2))
    (0, 1, 1, 1, 1, 1, 1)
    >>> tuple(digits(126, 16))
    (14, 7)
    """
    if x == 0: return
    yield x % b
    yield from to_base( x//b, b )
    #for d in to_base( x//b, b ):
    #    yield d

def to_base( x, b ):
    """Digits in a more typical order in a given base.

    >>> tuple(to_base(126, 2))
    (1, 1, 1, 1, 1, 1, 0)
    >>> bin(126)
    '0b1111110'
    >>> tuple(to_base(126, 16))
    (7, 14)
    >>> hex(126)
    '0x7e'

    >>> print( bin(126), tuple(to_base(126, 2)) )
    0b1111110 (1, 1, 1, 1, 1, 1, 0)
    >>> print( hex(126), tuple(to_base(126, 16)) )
    0x7e (7, 14)
    """
    return reversed( tuple(digits(x, b)) )

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    #performance()
