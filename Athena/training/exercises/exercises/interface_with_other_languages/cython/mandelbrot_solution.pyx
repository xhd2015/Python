"""
Mandelbrot Cython
-----------------

This exercise provides practice at writing a C extension module
using Cython.   The object of this is to take an existing Python
module and speed it up by re-writing it in Cython.

The code in this script generates a plot of the Mandelbrot set.

  1. The pure Python version of the code is contained in this file.
     Run this and see how long it takes to run on your system.

  2. The file mandelbrot.pyx contains the two functions mandelbrot_escape
     and generate_mandelbrot which are identical to the Python versions
     in this file.  Use the setup.py file to build a Cython module with
     the command::
     
        python setup.py build_ext --inplace
     
     and use the script mandelbrot_test.py to run the resulting code.
     How much of a speed-up (if any) do you get from compiling the
     unmodified Python code in Cython.
  
  3. Add variable typing for the scalar variables in the mandelbrot.pyx
     file.  Re-compile, and see how much of a speed-up you get.
     
  4. Turn the mandelbrot_escape function into a C only function.
     Re-compile, and see how much of a speed-up you get.

Bonus
~~~~~

Use the numpy Cython interface to optimize the code even further.
Re-compile, and see how much of a speed-up you get.

"""

from numpy import empty

cdef int mandelbrot_escape(double x, double y, int n):
    """ Mandelbrot set escape time algorithm in real and complex components
    """
    cdef double z_x = x
    cdef double z_y = y
    cdef int i
    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x, 2*z_x*z_y + y
        if z_x**2 + z_y**2 >= 4.0:
            break
    else:
        i = -1
    return i

def generate_mandelbrot(xs, ys, int n):
    """ Generate a mandelbrot set """
    cdef int i,j
    cdef int N = len(xs)
    cdef int M = len(ys)
    d = empty(dtype=int, shape=(len(xs), len(ys)))
    for j in range(M):
        for i in range(N):
            d[j,i] = mandelbrot_escape(xs[i], ys[j], n)
    return d
