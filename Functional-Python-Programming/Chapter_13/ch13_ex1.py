#!/usr/bin/env python3
"""Functional Python Programming

Chapter 13, Example Set 1
"""

year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
    (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
    (2008, 32.84), (2009, 33.02), (2010, 32.92)
    ]

fst = lambda x: x[0]
snd = lambda x: x[1]

from operator import *

test_itemgetter= """
>>> min( year_cheese, key=snd )
(2000, 29.87)
>>> max( year_cheese, key=itemgetter(1))
(2007, 33.5)
"""

from collections import namedtuple
YearCheese = namedtuple( "YearCheese", ("year", "cheese") )

year_cheese_2 = list(YearCheese(*yc) for yc in year_cheese)

test_attrgetter= """
>>> min( year_cheese_2, key=attrgetter('cheese') )
YearCheese(year=2000, cheese=29.87)
>>> max( year_cheese_2, key=lambda x: x.cheese )
YearCheese(year=2007, cheese=33.5)
"""

g_f = [1, 1/12, 1/288, -139/51840, -571/2488320, 163879/209018880, 5246819/75246796800]

g = [(1,1), (1,12), (1,288), (-139,51840),
    (-571,2488320), (163879,209018880),
    (5246819,75246796800)]

from itertools import starmap

from fractions import Fraction
test_starmap1 = """
>>> round( sum( starmap( truediv, g ) ), 6 )
1.084749
>>> round( sum( g_f ), 6 )
1.084749
>>> f= sum( Fraction(*x) for x in g )
>>> f
Fraction(81623851739, 75246796800)
>>> round( float(f), 6 )
1.084749
"""

from itertools import zip_longest

test_starmap2= """
>>> p = (3, 8, 29, 44)
>>> d = starmap( pow, zip_longest([], range(4), fillvalue=60) )
>>> pi = sum( starmap( truediv, zip( p, d ) ) )
>>> pi
3.1415925925925925
>>> d = starmap( pow, zip_longest([], range(4), fillvalue=60) )
>>> pi = sum( map( truediv, p, d ) )
>>> pi
3.1415925925925925
"""

def fact(n):
    """
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(4)
    24
    """
    f= { n == 0: lambda n: 1,
    n == 1: lambda n: 1,
    n == 2: lambda n: 2,
    n > 2: lambda n: fact(n-1)*n }[True]
    return f(n)

def semifact(n):
    """
    >>> semifact(0)
    1
    >>> semifact(1)
    1
    >>> semifact(2)
    2
    >>> semifact(3)
    3
    >>> semifact(4)
    8
    >>> semifact(5)
    15
    >>> semifact(9)
    945
    """
    alternatives= [(n == 0, lambda n: 1),
    (n == 1, lambda n: 1),
    (n == 2, lambda n: 2),
    (n > 2, lambda n: semifact(n-2)*n)]
    c, f= next(filter( itemgetter(0), alternatives ))
    return f(n)

def semifact2(n):
    """
    >>> semifact2(9)
    945
    """
    alternatives= [
        (lambda n: 1) if n == 0 else None,
        (lambda n: 1) if n == 1 else None,
        (lambda n: 2) if n == 2 else None,
        (lambda n: semifact2(n-2)*n) if n > 2 else None]
    f= next(filter(None, alternatives))
    return f(n)

def non_strict_max( a, b ):
    """
    >>> non_strict_max( 2, 2 )
    2
    >>> non_strict_max( 3, 5 )
    5
    >>> non_strict_max( 11, 7 )
    11
    """
    f = { a >= b: lambda: a, b >= a: lambda: b }[True]
    return f()

from itertools import count, takewhile
test_starmap3="""
>>> num= map( fact, count() )
>>> den= map( semifact, (2*n+1 for n in count()) )
>>> terms= takewhile( lambda t: t > 1E-10, map(truediv, num, den) )
>>> round( float(2*sum(terms)), 8 )
3.14159265
"""

test_reduction="""
>>> import functools, operator
>>> sum= functools.partial( functools.reduce, operator.add )
>>> sum([1,2,3])
6
>>> prod= functools.partial( functools.reduce, operator.mul )
>>> prod( [1,2,3,4] )
24
>>> fact= lambda n: 1 if n < 2 else n*prod( range(1,n) )
>>> fact(4)
24
>>> fact(0)
1
>>> fact(1)
1
"""

__test__ = {
    "test_itemgetter": test_itemgetter,
    "test_attrgetter": test_attrgetter,
    "test_starmap1": test_starmap1,
    "test_starmap2": test_starmap2,
    "test_starmap3": test_starmap3,
    "test_reduction": test_reduction,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()