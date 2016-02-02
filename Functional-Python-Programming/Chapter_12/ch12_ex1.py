#!/usr/bin/env python3
"""Functional Python Programming

Chapter 12, Example Set 1
"""
import math

def some_function(n, limit=1000, epsilon=1E-6):
    """
    >>> round(some_function(4),3)
    24.0
    """
    s= sum(
        (1,
        1/((2**1)*(6*n)**1),
        1/((2**3)*(6*n)**2),
        -139/((2**3)*(2*3*5)*(6*n)**3),
        -571/((2**6)*(2*3*5)*(6*n)**4),) )
    return math.sqrt(2*math.pi*n)*(n/math.e)**n*s

def test():
    import doctest
    doctest.testmod( )

def performance():
    import dis
    dis.disassemble(some_function.__code__)
    size= len(some_function.__code__.co_code)
    print( "size", size)

    import timeit
    t= timeit.timeit( """some_function(4)""", """from Chapter_12.ch12_ex1 import some_function""" )
    print( "time", t )

    print( "byte/sec", 1000000*size/t )

if __name__ == "__main__":
    test()
    performance()