# Pyrex sources to compute the sum of a sequence

cimport c_numpy
from c_numpy cimport import_array, ndarray, NPY_DOUBLE, \
                     PyArray_ContiguousFromAny

# intialize array module.
import_array()

def sum(object seq):
    """ Sum up the values in a sequence.
    """    
    # Declare type of ary variable.
    cdef ndarray ary
    cdef double *ary_data
    
    # object, data type, minimum dimension, maximum dimensions
    ary = PyArray_ContiguousFromAny(seq, NPY_DOUBLE, 1, 1)
    ary_data = <double *>ary.data

    # How long is the array in the first dimension?
    n = ary.dimensions[0]

    cdef int i
    cdef double sum
    
    sum = 0.0
    for i from 0 <= i < n:
        sum = sum + ary_data[i]
        
    return sum    