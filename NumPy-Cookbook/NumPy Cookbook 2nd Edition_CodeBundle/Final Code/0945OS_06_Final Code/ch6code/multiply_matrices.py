import numpy as np
import numpy.core.umath_tests as ut 

x = np.ones((10, 2, 4)) 
y = np.ones((10, 4, 5)) 
print ut.matrix_multiply(x, y).shape
