REM Put the Python installation directory as the first command line argument
REM of this .bat file.  E.g.
REM > build_pysimpson.bat C:\Python27
REM
REM Compile the Fortran library.
gfortran -std=f95 -pedantic -c types.f90
gfortran -std=f95 -pedantic -c simpson.f90

REM Compile the wrapper.
gfortran -std=f2003 -pedantic -c simpson_wrapper.f90

REM Build the Python extension module...

REM First run cython to generate the C extension.
cython pysimpson.pyx

REM Compile the C extension module.
gcc -I%1\include -c pysimpson.c

REM Build the shared library.  Use 'import pysimpson' in python.
gcc -shared pysimpson.o simpson_wrapper.o simpson.o types.o -L%1\libs -lpython27 -o pysimpson.pyd

REM Clean up
del *.o *.mod pysimpson.c
