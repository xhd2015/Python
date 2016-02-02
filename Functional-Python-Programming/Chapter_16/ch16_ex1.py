#!/usr/bin/env python3
"""Functional Python Programming

Chapter 16, Example Set 1
"""
from functools import reduce
from operator import mul

prod = lambda x: reduce( mul, x )

from collections.abc import Callable
class Binomial( Callable ):
    """
    >>> binom= Binomial()
    >>> binom(52,5)
    2598960
    """
    def __init__( self ):
        self.fact_cache= {}
        self.bin_cache= {}
    def fact( self, n ):
        if n not in self.fact_cache:
            self.fact_cache[n]= prod( range(1,n+1) )
        return self.fact_cache[n]
    def __call__( self, n, m ):
        if (n,m) not in self.bin_cache:
            self.bin_cache[n,m]= self.fact(n)//(self.fact(m)*self.fact(n-m))
        return self.bin_cache[n,m]

test_example="""
>>> binom= Binomial()
>>> binom(52,5)
2598960
"""

__test__ = {
    "test_example": test_example,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
