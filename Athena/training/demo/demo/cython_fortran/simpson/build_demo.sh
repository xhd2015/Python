#!/bin/sh

set -x

# Compile the Fortran library.
gfortran -std=f95 -pedantic -c types.f90
gfortran -std=f95 -pedantic -c simpson.f90

# Compile the Fortran demo.
# Use ./demo to run it.
gfortran -std=f95 -pedantic -c demo.f90
gfortran demo.o simpson.o types.o -o demo

# Compile the wrapper.  The wrapper uses the ISO C bindings
# feature of Fortran 2003.
gfortran -std=f2003 -pedantic -c simpson_wrapper.f90

# Compile the C demo, and build the executable using gfortran.
gcc -Wall -pedantic -c demo_wrapper.c
gfortran demo_wrapper.o simpson_wrapper.o simpson.o types.o -o demo_wrapper

# Clean up
rm -rf *.o *.mod
