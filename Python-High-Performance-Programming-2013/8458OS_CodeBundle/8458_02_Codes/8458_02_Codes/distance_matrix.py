import numpy as np
import numexpr as ne

def distance_matrix_numpy(size):
    r = np.random.rand(size, 2)
    r_i = r[:, np.newaxis]
    r_j = r[np.newaxis, :]

    d_ij = np.sqrt(((r_i - r_j)**2).sum(axis=2))

def distance_matrix_numexpr(size):
    r = np.random.rand(size, 2)
    r_i = r[:, np.newaxis]
    r_j = r[np.newaxis, :]

    d_ij = ne.evaluate("sum((r_i - r_j)**2, 2)")
    d_ij = ne.evaluate("sqrt(d_ij)")

