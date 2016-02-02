#!/usr/bin/env python3
"""Functional Python Programming

Chapter 8, Example Set 2
"""
from itertools import *

source = zip( count(0, .1), (.1*c for c in count()) )
neq = lambda x, y: abs(x-y) > 1.0E-12

def until( terminate, iterator ):
    i = next(iterator)
    if terminate(*i): return i
    return until( terminate, iterator )

accumulated_error_1= """
>>> print( until(neq, source) )
(92.799999999999, 92.80000000000001)
"""

def until_i( terminate, iterator ):
    for i in iterator:
        if terminate(*i): return i

accumulated_error_2= """
>>> source = zip( count(0, .1), (.1*c for c in count()) )
>>> print( until_i(lambda x, y: abs(x-y) > 1.0E-6, source) )
(94281.30000100001, 94281.3)
>>> source_3 = zip( count(0, 1/35), (c/35 for c in count()) )
>>> print( until_i(lambda x, y: abs(x-y) > 1.0E-6, source_3) )
(73143.51428471429, 73143.5142857143)
>>> source_3 = zip( count(0, 1/35), (c/35 for c in count()) )
>>> print( until_i(lambda x, y: x != y, source_3 ) )
(0.2285714285714286, 0.22857142857142856)
"""

fizz_buzz= """
# Silly fizz-buzz-like problem.
>>> m3= ( i == 0 for i in cycle( range(3) ) )
>>> m5= ( i == 0 for i in cycle( range(5) ) )
>>> multipliers = zip( range(10), m3, m5 )
>>> total = sum(i for i, *multipliers in multipliers
...    if any(multipliers))
>>> print( total )
23
"""

import io, csv

file_filter="""
>>> chooser = (x == 0 for x in cycle(range(3)))
>>> with open("Anscombe.txt") as source_file:
...    rdr= csv.reader( source_file, delimiter="\\t" )
...    #keep= (row for pick, row in zip(chooser, rdr) if pick)
...    keep= tuple( compress( rdr, chooser ) )
>>> for row in keep:
...    print( row )
["Anscombe's quartet"]
['10.0', '8.04', '10.0', '9.14', '10.0', '7.46', '8.0', '6.58']
['9.0', '8.81', '9.0', '8.77', '9.0', '7.11', '8.0', '8.84']
['6.0', '7.24', '6.0', '6.13', '6.0', '6.08', '8.0', '5.25']
['7.0', '4.82', '7.0', '7.26', '7.0', '6.42', '8.0', '7.91']
"""

# Repeat
#all = repeat(0)
#subset= cycle(range(100))
#randomized= random.randrange(100)
#chooser = (x == 0 for x in all_or_subset_or_randomized)

squares= """
>>> squares = list(sum(repeat(i, times=i)) for i in range(10))
>>> print( squares )
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""

__test__ = {
    "accumulated_error_1": accumulated_error_1,
    "accumulated_error_2": accumulated_error_2,
    "fizz_buzz": fizz_buzz,
    "file_filter": file_filter,
    "squares": squares,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
