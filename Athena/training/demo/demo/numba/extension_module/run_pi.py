import ctypes
from ctypes import c_double, c_int32

lib=ctypes.CDLL('/home/pberkes/del/numba_examples/extension_module/pi.so')

lib.mult.restype=c_double
lib.mult.argtypes=[c_int32]

print lib.mult(2)     # prints 6.28318530718
#lib.mult(3.2)          gives error


lib.mult_f.restype=c_double
lib.mult_f.argtypes=[c_double]

print lib.mult_f(2)   # prints 6.28318530718
print lib.mult_f(3.2) # prints 10.0530964915
