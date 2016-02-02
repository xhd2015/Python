"""before.py -- run this code through pyflakes and pep8."""

from math import sin, cos

class Foo(object):
    def some_method(self):
        """docstring for some_method"""
        pass
    
def bar(x):
    """docstring for bar function""" 

    y=sin(x*x +1)
    z = acos(y)
    return y-pi