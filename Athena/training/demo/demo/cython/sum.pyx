#cython: boundscheck=False
# Cython sources to compute the sum of a sequence

cimport numpy as np

def sum(np.ndarray[np.float64_t] ary):
    """ Sum up the values in a sequence.
    """        
    # How long is the array in the first dimension?
    cdef int n = ary.shape[0]

    cdef unsigned int i
    cdef double sum
    
    sum = 0.0
    for i in range(0, n):
        sum = sum + ary[i]
        
    return sum    