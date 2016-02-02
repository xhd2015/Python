"""
ctypes
------

"""

import ctypes
from numpy import array, dtype, float32, float64, asarray, require
from numpy.ctypeslib import load_library, ndpointer

# 2. Load libfib; call it libfib.

libfib = ctypes.CDLL('libfib')
# or use numpy.ctypeslib.load_library():
# libfib = load_library('libfib','.')

# 3. Set the argtypes attribute of the fib function, and
#    compute fib(10)

libfib.fib.argtypes = [ctypes.c_int]

m = libfib.fib(10)
print "The tenth Fibonacci number is", m

# 4. Demonstrate that passing a non-integer argument raises
#    an exception.

try:
    m = libfib.fib("ten")
except ctypes.ArgumentError, e:
    print "Caught the ArgumentError exception,", e


# 5.  Create a wrapper for _sum().

# First set the result type and argtypes of the _sum function.
# Use numpy.ctypeslib.ndpointer to tell ctypes the type of the
# array pointer argument.

libfib._sum.restype = ctypes.c_float
libfib._sum.argtypes = [ndpointer(dtype=float32, ndim=1, 
                                        flags='C_CONTIGUOUS'),
                        ctypes.c_int] 

# sum() is a wrapper for libfib._sum.  Since we know the length
# of the numpy array, there is no need for a user to provide a
# length argument.  Also, we will use the numpy function `asarray`
# to convert the argument to a numpy array if it isn't one already.
# This allows a call such as
#   s = sum([1.0, 2.0, 3.0])

def sum(ary):
    ary = asarray(ary, dtype=float32)
    return libfib._sum(ary, len(ary))

# Some examples of using sum()

val1 = array((1,2,3,4,5,6,7), dtype=float32)
s = sum(val1)
print
print "val1 is", val1
print "sum(val1) is", s

lst = [1.0, 2.0, 3.0]
m = sum(lst)
print "sum(%s) = %f" % (lst,m)


# 6. Create a wrapper for _sum2().

# Use a structured dtype to match the C structure.
coord_dtype = dtype([('x',float64),('y',float64)])

libfib._sum2.restype = ctypes.c_double
libfib._sum2.argtypes = [ndpointer(dtype=coord_dtype, ndim=1, 
                                        flags='C_CONTIGUOUS'),
                        ctypes.c_int]

# Define the python wrapper sum2().  We use the numpy function
# `require` to ensure that the argument is a numpy array of the
# appropriate type.

def sum2(ary):
    ary = require(ary, dtype=coord_dtype, requirements=['C_CONTIGUOUS'])
    return libfib._sum2(ary, len(ary))

val2 = array([(1,2),(2,3)], dtype=coord_dtype)
s = sum2(val2)
print
print "val2 is", val2
print "sum2(val2) is", s
