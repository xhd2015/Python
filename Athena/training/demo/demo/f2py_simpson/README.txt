
simpson.f
    Fortran 77 function SIMPSON applies the composite Simpson's rule to
    a function.

demo.f
    Fortran 77 program to the demonstrates the use of the function SIMPSON.

build.sh
    Contains the f2py command to builld an extension module that wraps
    simpson.f.

demo_pysimpson.py
    Demonstration the use of the Python extension module created by f2py.
