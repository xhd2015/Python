"""
Mandelbrot Cython
-----------------

This exercise provides practice at writing a C extension module
using Cython.   The object of this is to take an existing Python
module and speed it up by re-writing it in Cython.

The code in this script (mandelbrot.py) generates a plot of the
Mandelbrot set.

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


See :ref:`mandelbrot_solution1` and :ref:`mandelbrot_solution2` and :ref:`mandelbrot_solution3`.
"""

from numpy import empty

def mandelbrot_escape(x, y, n):
    """ Mandelbrot set escape time algorithm in real and complex components
    """
    z_x = x
    z_y = y
    for i in range(n):
        z_x, z_y = z_x**2 - z_y**2 + x, 2*z_x*z_y + y
        if z_x**2 + z_y**2 >= 4.0:
            break
    else:
        i = -1
    return i

def generate_mandelbrot(xs, ys, n):
    """ Generate a mandelbrot set """
    d = empty(shape=(len(ys), len(xs)))
    for j in range(len(ys)):
        for i in range(len(xs)):
            d[j,i] = mandelbrot_escape(xs[i], ys[j], n)
    return d


if __name__ == '__main__':
    import time
    from numpy import r_
    from matplotlib.pyplot import imshow, show, cm

    x = r_[-2:1:100j]
    y = r_[-1.5:1.5:100j]

    t = time.time()
    d = generate_mandelbrot(x, y, 100)
    print 'Execution time:', time.time() - t

    imshow(d, extent=[-2,1,-1.5,1.5], cmap=cm.gist_stern)
    show()
