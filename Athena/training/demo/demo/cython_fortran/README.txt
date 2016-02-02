first_example/

    This directory contains an example of a Fortran function with C bindings.
    A C program is provided that calls the Fortran function.

    first_example.f90
        Simple example of C binding for a Fortran function.
    first_example_main.c
        C program that calls the function in first_example.f90
    first_example_build.sh
        Commands to compile the example (Linux)


functions/

    In this demo, Cython is used to wrap a Fortran function.  The Cython
    wrapper takes a NumPy array as an argument.

    functions.f90
        Defines the Fortran subroutine sinc1d.
    functions_wrapper.f90
        Provides a Fortran wrapper of sinc1d with C bindings, called c_sinc1d.
    pyfunctions.pyx
        A Cython file that wraps c_sinc1d.
    build_pyfunctions.sh
        Script to build the Python extension module.


simpson/

    This directory contains an example of a Fortran function that takes a
    function as an argument (i.e. a "callback").  In the Python wrapper,
    the user must provide a Python function.  This demo shows one way to
    implement such an interface.

    types.f90
    simpson.f90
        The Fortran "library" code to be wrapped.  In this
        example, the only function in the library is simpson.

    demo.f90
        Fortran main program to demonstrate the Fortran library:
        (This file is not used when wrapping the library in C.)

    simpson_wrapper.f90
        Fortran wrapper of the simpson function, with C bindings.

    demo_wrapper.c
        C program that demonstrates the use of the C wrapper of simpson.
        (This file is not used in the Python wrapper.)

    pysimpson.pyx
        Cython wrapper of the C simpson_wrapper.

    demo_pysimpson.py
        Demo the python extension module.

    build_demo.sh
        Build Fortran and C demos (Linux)
    build_pysimpson.sh
        Build extension module for Python (Linux)
    build_pysimpson.bat
        Build extension module for Python (Windows)
        Include the installation directory (e.g. C:\Python27)
        as the first command line argument of the .bat file.
