from __future__ import print_function
import numpy as np

def double(a):
   return 2 * a

ufunc = np.frompyfunc(double, 1, 1)
print("Result", ufunc(np.arange(4)))
