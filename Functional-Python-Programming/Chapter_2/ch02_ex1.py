#!/usr/bin/env python3
"""Functional Python Programming

Chapter 2, Example Set 1
"""

def higher_order():
    """Higher Order Functions."""

    year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
        (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
        (2008, 32.84), (2009, 33.02), (2010, 32.92)
        ]

    max( year_cheese )
    max( year_cheese, key= lambda yc: yc[1] )
    max(map(lambda yc: (yc[1],yc), year_cheese))

def namedtuples():
    """nametuple vs. class performance"""
    import timeit
    print( "class", timeit.timeit("""x= X(1,2,3)""",
    """
class X:
    def __init__( self, a, b, c ):
        self.a= a
        self.b= b
        self.c= c
    """) )

    print( "tuple", timeit.timeit("""x= (1,2,3)""") )

    print( "namedtuple", timeit.timeit("""x= X(1,2,3)""",
    """
from collections import namedtuple
X= namedtuple( "X", ("a", "b", "c") )
    """) )

def sum_non_strict():
    """Non-strict generators."""

    def numbers():
        for i in range(1024):
            print( "=", i )
            yield i

    def sum_to(n):
        sum= 0
        for i in numbers():
            if i == n: break
            sum += i
        return sum

import math
def isprimei( n ):
    """Is n prime?

    >>> isprimei(2)
    True
    >>> tuple( isprimei(x) for x in range(3,11) )
    (True, False, True, False, True, False, False, False)
    """
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3,1+int(math.sqrt(n)),2):
        if n % i == 0:
            return False
    return True

def isprimer(n):
    """Is n prime?

    >>> isprimer(2)
    True
    >>> tuple( isprimer(x) for x in range(3,11) )
    (True, False, True, False, True, False, False, False)
    """
    def isprime(k, coprime):
        """Is k relatively prime to the value coprime?"""
        if k < coprime*coprime: return True
        if k % coprime == 0: return False
        return isprime(k, coprime+2)

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime(n, 3)

def isprimeg( n ):
    """Is n prime?

    >>> isprimeg(2)
    True
    >>> tuple( isprimeg(x) for x in range(3,11) )
    (True, False, True, False, True, False, False, False)

    Remarkably slow for large primes, for example, M_61=2**61-1.
    """
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return not any(n%p==0 for p in range(3,int(math.sqrt(n))+1,2))

def recursion():
    """Recursion Performance Comparison.
    """
    import timeit
    print( "isprimei", timeit.timeit( "isprimei(131071)", """
import math
def isprimei( n ):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3,1+int(math.sqrt(n)),2):
        if n % i == 0:
            return False
    return True
    """, number=100000 ) )
    print( "isprimer", timeit.timeit( """isprimer(131071)""", """
def isprimer( n ):
    def isprime( n, coprime ):
        if n < coprime*coprime: return True
        if n % coprime == 0: return False
        return isprime( n, coprime+2 )

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime( n, 3 )
    """, number=100000 ) )
    print( "isprimeg", timeit.timeit( """isprimeg(131071)""", """
import math
def isprimeg( n ):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return not any(n%p==0 for p in range(3,int(math.sqrt(n))+2))
    """, number=100000 ) )

def limit_of_performance():
    """We can see that testing a large prime is
    quite slow. Testing large non-primes is quite fast.
    """
    import time

    t= time.perf_counter()
    for i in range(30,89):
        m= 2**i-1
        print( i, m, end="" )
        if isprimeg( m ):
            print( "prime", end="" )
        else:
            print( "composite", end="" )
        print( time.perf_counter() - t )

def test():
    """
    >>> isprimei(131071)
    True
    >>> isprimer(131071)
    True
    >>> isprimeg(131071)
    True
    """
    import doctest
    doctest.testmod(verbose=2)

if __name__ == "__main__":
    namedtuples()
    #recursion()
    #limit_of_performance()
    test()
