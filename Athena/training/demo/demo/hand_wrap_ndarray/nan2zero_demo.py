
from numpy import array, nan, float32, float64
from nan2zero import nan_to_zero

x = array([-10.0, 5.0, nan, 20.0, nan])

print "before: x =", x
nan_to_zero(x)
print "after:  x =", x

y = array([[50.0, 60.0, nan],[20.0, nan, 95.0]], dtype=float32)

print
print "before: y ="
print y
nan_to_zero(y)
print "after:  y ="
print y

print
z = array([1, 2, 3])
try:
    nan_to_zero(z)
except ValueError as err:
    print "As expected, passing an integer array to nan_to_zero()"
    print "resulted in a ValueError exception:"
    print "   ", err

print
x2 = x[::2]
try:
    nan_to_zero(x2)
except ValueError as err:
    print "As expected, passing a noncontiguous array to nan_to_zero()"
    print "resulted in a ValueError exception:"
    print "   ", err
