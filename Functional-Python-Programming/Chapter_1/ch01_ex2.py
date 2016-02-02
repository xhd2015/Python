#!/usr/bin/env python3
"""Functional Python Programming

Chapter 1, Example Set 2

Newton-Raphson root-finding via bisection.

http://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf

Translated from Miranda to Python.
"""

# next_ = lambda n, x: (x+n/x)/2

def next_(n, x):
    """
    ..  math::

        a_{i+1} = (a_i+n/a_i)/2

    Converges on

    ..  math::

        a = (a+n/a)/2

    So

    ..  math::

        2a  &= a+n/a \\
        a   &= n/a \\
        a^2 &= n \\
        a   &= \sqrt n
    """
    return (x+n/x)/2

def repeat(f, a):
    yield a
    yield from repeat(f, f(a) )
    #for v in repeat( f, f(a) ):
    #    yield v

def within(ε, iterable):
    def head_tail(ε, a, iterable):
        b= next(iterable)
        if abs(a-b)<=ε: return b
        return head_tail( ε, b, iterable )
    return head_tail( ε, next(iterable), iterable )

def sqrt(a0, ε, n):
    return within( ε, repeat( lambda x: next_(n,x), a0 ) )

def test():
    """
    >>> round(next_( 2, 1.5 ), 4)
    1.4167
    >>> n= 2
    >>> f= lambda x: next_( n, x )
    >>> a0= 1.0
    >>> [ round(x,4) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))),) ]
    [1.0, 1.5, 1.4167, 1.4142]

    >>> within( .5, iter([3, 2, 1, .5, .25]) )
    0.5

    >>> round( sqrt( 1.0, .0001, 3 ), 6 )
    1.732051
    >>> round(1.732051**2, 5)
    3.0
    """
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
