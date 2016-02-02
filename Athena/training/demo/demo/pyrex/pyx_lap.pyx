# Pyrex sources to compute the laplacian.
# Some of this code is taken from numeric_demo.pyx
#
# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
#         Eric Jones <eric at enthought dot com>

cimport c_numpy
from c_numpy cimport import_array, ndarray, npy_intp, NPY_DOUBLE, \
                     PyArray_ContiguousFromAny

# intialize array module.
import_array()

# we need sqrt for calculating the actual error.
cdef extern from "math.h":
    double sqrt(double x)

def pyrexTimeStep(object ou, double dx, double dy):
    # convert ou to a contiguous double precision numpy array with 
    # mindim=2 and maxdim=2
    cdef ndarray u
    u = PyArray_ContiguousFromAny(ou, NPY_DOUBLE, 2, 2)
    
    
    # get the nx and ny values from the numpy array dimensions.
    cdef npy_intp nx, ny
    nx = u.dimensions[0]
    ny = u.dimensions[1]

    # now cast the data pointer in the numpy array to a double*
    # pointer
    cdef double *elem
    elem = <double *>u.data
    
    cdef double dx2, dy2, dnr_inv, err
    dx2, dy2 = dx**2, dy**2
    dnr_inv = 0.5/(dx2 + dy2)    
    err = 0.0
    
    cdef int i, j
    cdef double diff, tmp
    
    # pointers to the center, right, left, up, and down
    # stencil elements of the data array.
    cdef double *uc, *uu, *ud, *ul, *ur
    
    for i from 1 <= i < nx-1:
        uc = elem + i*ny + 1
        ur = elem + i*ny + 2
        ul = elem + i*ny
        uu = elem + (i+1)*ny + 1
        ud = elem + (i-1)*ny + 1
        
        for j from 1 <= j < ny-1:
            tmp = uc[0]
            uc[0] = ((ul[0] + ur[0])*dy2 +
                     (uu[0] + ud[0])*dx2)*dnr_inv
            diff = uc[0] - tmp
            err = err + diff*diff
            uc = uc + 1; ur = ur + 1;  ul = ul + 1
            uu = uu + 1; ud = ud + 1

    return sqrt(err)
