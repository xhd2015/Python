
import numpy as np
from nan2zero import nan_to_zero_float, nan_to_zero_double


x = np.array([1.0, np.nan, 10.0, -1, np.nan])
print "Before:", repr(x)

nan_to_zero_double(x)

print "After: ", repr(x)
print


y = np.array([0.5, 1.0, np.nan, np.nan, -1.0], dtype=np.float32)
print "Before:", repr(y)

nan_to_zero_float(y)

print "After: ", repr(y)
print
