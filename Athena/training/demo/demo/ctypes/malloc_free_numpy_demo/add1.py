
import sys

from numpy import ctypeslib
from numpy import array, float32
from ctypes import c_float, c_int, POINTER, CDLL, util

def cfree(mem):
    """Free memory allocated by malloc in the call to add1()."""
    libc_name = util.find_library('c')
    libc = CDLL(libc_name)
    libc.free.restype = None
    libc.free.argtypes = [POINTER(None)]
    libc.free(mem)

# Load the shared library.  The filename is platform-dependent.        
if sys.platform == 'win32':
    lib = ctypeslib.load_library('libadd1.dll', '.')
else:
    lib = ctypeslib.load_library('libadd1.so', '.')

# Set the argument and result types of add1().
lib.add1.restype = POINTER(c_float)
ptr = ctypeslib.ndpointer(float32, ndim=1, flags='C')
lib.add1.argtypes = [ptr, c_int]

# Test it.
x = array([1, 2, 3, 4], dtype=float32)
print "x   =", x

res = lib.add1(x, len(x))
arr = ctypeslib.as_array(res, x.shape)

print "arr =", arr

# Free the memory that was allocated by add1().
# This mean that arr, and any other arrays that
# had views of the data in arr, if there were any,
# will have invalid data.
cfree(res)
