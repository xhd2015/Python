#cython: boundscheck=False
#  
# Cython sources to compute the laplacian.
# Some of this code is taken from numeric_demo.pyx
#
# Author: Prabhu Ramachandran <prabhu_r at users dot sf dot net>
#         Eric Jones <eric at enthought dot com>

cimport numpy as np

#initialize NumPy C-API
np.import_array()

# we need sqrt for calculating the actual error.
cdef extern from "math.h":
    double sqrt(double x)

def cythonTimeStep(object ou, double dx, double dy):
    # convert ou to a contiguous double precision numpy array with 
    # mindim=2 and maxdim=2
    cdef np.ndarray[np.npy_double, ndim=2] u
    u = np.PyArray_ContiguousFromAny(ou, np.NPY_DOUBLE, 2, 2)
    
    
    # get the nx and ny values from the numpy array dimensions.
    cdef np.npy_intp nx, ny
    nx = u.shape[0]
    ny = u.shape[1]
    
    cdef double dx2, dy2, dnr_inv, err
    dx2, dy2 = dx**2, dy**2
    dnr_inv = 0.5/(dx2 + dy2)    
    err = 0.0
    
    cdef unsigned int i, j
    cdef double diff, tmp
        
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            tmp = u[i,j]
            u[i,j] = ((u[i,j-1] + u[i,j+1])*dy2 +
                     (u[i-1,j] + u[i+1,j])*dx2)*dnr_inv
            diff = u[i,j] - tmp
            err = err + diff*diff
 
    return sqrt(err)
