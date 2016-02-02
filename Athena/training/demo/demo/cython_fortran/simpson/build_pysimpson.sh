#!/bin/sh

set -x

PYCFLAGS=`python-config --cflags`
PYLIBS=`python-config --libs`
PYLIBDIR=`python-config --prefix`/lib
NUMPY_INCLUDE=-I`python -c "import numpy; print numpy.get_include()"`

# Compile the Fortran library.
gfortran $PYCFLAGS -std=f95 -pedantic -c -fPIC types.f90
gfortran $PYCFLAGS -std=f95 -pedantic -c -fPIC simpson.f90

# Compile the wrapper.
gfortran $PYCFLAGS -std=f2003 -pedantic -c -fPIC simpson_wrapper.f90

# Build the Python extension module...

# First run cython to generate the C extension.
cython pysimpson.pyx

# Compile the C extension module.
gcc $PYCFLAGS $NUMPY_INCLUDE -c -fPIC pysimpson.c
gcc -shared pysimpson.o simpson_wrapper.o simpson.o types.o $PYCFLAGS $PYLIBS -L$PYLIBDIR -o pysimpson.so

# Clean up
rm -rf *.o *.mod pysimpson.c
