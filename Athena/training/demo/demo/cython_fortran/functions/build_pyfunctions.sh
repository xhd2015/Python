#!/bin/sh

set -x

PYCFLAGS=`python-config --cflags`
PYLIBS=`python-config --libs`
PYLIBDIR=`python-config --prefix`/lib
NUMPY_INCLUDE=-I`python -c "import numpy; print numpy.get_include()"`

# Compile the fortran source files.  We have to use the same PYCFLAGS here to
# ensure we compile for the correct architecture (64 vs 32 bit).
gfortran $PYCFLAGS -std=f95 -pedantic -c -fPIC functions.f90
gfortran $PYCFLAGS -std=f2003 -pedantic -c -fPIC functions_wrapper.f90

# Generate the C extension module from the Cython source file.
cython pyfunctions.pyx

# Compile the C extension module.
gcc $PYCFLAGS $NUMPY_INCLUDE -c -fPIC pyfunctions.c
gcc -shared pyfunctions.o functions_wrapper.o functions.o $PYCFLAGS $PYLIBS -L$PYLIBDIR -o pyfunctions.so

# Clean up
rm -rf *.o *.mod pyfunctions.c
