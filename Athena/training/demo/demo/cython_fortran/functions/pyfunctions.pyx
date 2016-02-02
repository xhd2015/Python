import numpy as np
cimport numpy as np

cdef extern:
    void c_sinc1d(int n, double *x, double *y)


def sinc1d(x):
    cdef np.ndarray[np.double_t, ndim=1, mode="c"] x_c
    cdef np.ndarray[np.double_t, ndim=1] y

    x_c = np.ascontiguousarray(x, dtype=np.double)
    y = np.empty_like(x_c)
    c_sinc1d(x_c.size, &x_c[0], &y[0])
    return y
