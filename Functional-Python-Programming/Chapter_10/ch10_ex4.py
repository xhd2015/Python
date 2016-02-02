#!/usr/bin/env python3
"""Functional Python Programming

Chapter 10, Example Set 4
"""

from functools import reduce, partial
import math

display= lambda iterable: reduce( lambda x,y: print(x,y), iterable )
sum2= lambda iterable: reduce( lambda x,y: x+y**2, iterable, 0 )
sum= lambda iterable: reduce( lambda x, y: x+y, iterable )
count= lambda iterable: reduce( lambda x, y: x+1, iterable, 0 )
min= lambda iterable: reduce( lambda x, y: x if x < y else y, iterable )
max= lambda iterable: reduce( lambda x, y: x if x > y else y, iterable )

test_reductions="""
>>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
>>> sum2(d)
232
>>> sum(d)
40
>>> count(d)
8
>>> sum(d)/count(d)
5.0
>>> math.sqrt((sum2(d)/count(d))-(sum(d)/count(d))**2)
2.0
>>> max(d)
9
>>> min(d)
2
"""

def map_reduce( map_fun, reduce_fun, iterable ):
    return reduce( reduce_fun, map( map_fun, iterable ) )

def sum2_mr( iterable ):
    """
    >>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
    >>> sum2_mr(d)
    232
    """
    return map_reduce( lambda y: y**2, lambda x,y: x+y, iterable )

import operator
def sum2_mr2( iterable ):
    """
    >>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
    >>> sum2_mr2(d)
    232
    """
    return map_reduce( lambda y: y**2, operator.add, iterable )

def count_mr( iterable ):
    """
    >>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
    >>> count_mr(d)
    8
    """
    return map_reduce( lambda y: 1, lambda x,y: x+y, iterable )

def comma_fix( data ):
    try:
        return float(data)
    except ValueError:
        return float(data.replace(",",""))

def clean_sum( cleaner, data ):
    """
    >>> d = '1,196', '1,176', '1,269', '1,240', '1,307', '1,435', '1,601', '1,654', '1,803', '1,734'
    >>> clean_sum( comma_fix, d )
    14415.0
    """
    return reduce( operator.add, map( cleaner, data ) )

sum_p =  partial( reduce, operator.add )

test_sump = """
>>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
>>> sum_p(d)
40
>>> sum_p( map(lambda x:x**2, d) )
232
"""

def performance():
    import timeit
    r = timeit.timeit( """reduce( operator.add, ["1", ",", "2", ",", "3"], "" )""", """from functools import reduce; import operator""")
    j = timeit.timeit( """''.join( ["1", ",", "2", ",", "3"] )""")
    print( 'reduce', r )
    print( 'join', j )

__test__ = {
    "test_reductions": test_reductions,
    "test_sump": test_sump,
}

def test():
    import doctest
    doctest.testmod( verbose=1 )

if __name__ == "__main__":
    test()
    performance()