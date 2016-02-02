from numba import autojit
import numpy as np


@autojit
def matrix_vector(M, v):
    return np.sum(M * v, axis=1)


M = np.arange(90).reshape(9, 10)
v = np.arange(10)
print matrix_vector(M, v)
print np.dot(M, v)
