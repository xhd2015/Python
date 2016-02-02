"""
The modf() function in the C math library has the signature

    double modf(double x, double *intpart)

Given x, modf returns the fractional part of x, and stores the
integer part of x in the location pointed to by intpart.

This file uses ctypes to implement the python function modf(x) that
returns a tuple containing the integer and fractional parts of x.

This example demonstrate the use of c_double() and byref() from ctypes.
If you really need the modf function, it is available as math.modf
"""

from ctypes import util, c_double, c_void_p, CDLL, byref

# Find and load the math library.
_libname = util.find_library('m')
_libm = CDLL(_libname)

# Set the argument and return types of the math library's modf function.
_libm.modf.argtypes = [c_double, c_void_p]
_libm.modf.restype = c_double


def modf(x):
    """
    Returns a tuple containing the fractional and integer parts of the
    floating point value x.  For example,
    >>> modf(17.25)
    (0.25, 17.0)
    """
    # Create a ctypes double object.  This can be given to byref() to create
    # a reference to the double value.
    i = c_double()
    frac = _libm.modf(x, byref(i))
    return frac, i.value


if __name__ == "__main__":
    x = 17.25
    print "x =", x
    print "modf(x) =", modf(x)
