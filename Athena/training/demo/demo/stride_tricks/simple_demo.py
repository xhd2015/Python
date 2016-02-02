from numpy import arange 
from numpy.lib.stride_tricks import as_strided

a = arange(1,15)
print "a:"
print a
print

b = as_strided(a, (11,4), (4,4))
print "b:"
print b
