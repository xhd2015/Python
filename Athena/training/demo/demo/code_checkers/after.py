"""after.py -- clean version of before.py"""

from math import sin, acos, pi


class Foo(object):
    def some_method(self):
        """docstring for some_method"""
        pass


def bar(x):
    """docstring for bar function"""

    y = sin(x * x + 1)
    z = acos(y)
    return z - pi
