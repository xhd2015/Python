import math
from pysimpson import simpson

a = 0.0
b = 2.0
n = 100
intgrl = simpson(math.cos, a, b, n)
print "integrate cos"
print "simpson: ", intgrl
print "exact:   ", math.sin(b) - math.sin(a)
print


def func(x, y):
    return x + y ** 2


def int_over_x(y, a, b, n):
    result = simpson(lambda x: func(x, y), a, b, n)
    return result


def volume(a, b, c, d, n):
    result = simpson(lambda y: int_over_x(y, a, b, n), c, d, n)
    return result


a = 0
b = 6
c = 0
d = 3
print "2D iterated integral"
print "volume:", volume(a, b, c, d, n)
exact = 0.5 * (d - c) * (b - a) ** 2 + (1. / 3) * (d ** 3 - c ** 3) * (b - a)
print "exact: ", exact
