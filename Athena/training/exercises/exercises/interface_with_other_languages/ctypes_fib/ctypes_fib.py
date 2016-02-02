""" 
ctypes
------

The file fib.c contains three C functions:

    int fib(int n)
        Computers the nth number in the Fibonacci sequence.

    float _sum(float* val, int length)
        Computes the sum of the array of floats at `val`.
        `length` is the size of the array.

    double _sum2(coord* val, int length)
        Computes the sum of the x and y coordinates of all the
        elements in the array of coords.  `coord` is a C structure
        with two double fields, `x` and `y`.
        `length` is the size of the array.


1. Build the libfib shared library using the appropriate build script:
   build_fib.bat in Windows, build_fib_macosx.sh in Mac OSX, or
   build_fib.sh in Linux.
2. In python, load the libfib shared library.  This is done for you
   in the code below.
3. Set the argtypes attributes of the fib function so that
   it accepts only an integer.  Use the fib function to find the
   tenth Fibonacci number.
4. Verify that passing a non-integer argument to the fib
   function raises an exception.  (If you are creating a script
   containing your complete solution, you can enclose your
   invalid use of fib() in a try/except statement.)
5. Create a python function called sum() that takes as its single
   argument a numpy array, or a list or tuple of numbers. The
   function must take this argument and convert it to a numpy array
   that can be passed to _sum().  There is no need for sum() to be
   given the length of the array.  Instead, it should compute the
   length of its argument and pass it to _sum().
6. BONUS: Create a python function called sum2() that takes as its
   single argument a numpy structured array with a dtype containing
   two fields of type float64 and that calls _sum2() with an
   appropriate pair of arguments.

See :ref:`ctypes-fib-solution`.
"""


import ctypes
from numpy import array, asarray, float32, require

def load_fib():
    '''
    Returns the loaded libfib library, appropriate for your platform.  Raises a
    RuntimeError if unsucessful.

    '''
    # Note: While instructive, understanding the internals of this function is
    # not part of this exercise; it is provided here for you to use, and will
    # work no matter what platform you are on (provided you have previously
    # compiled the libfib library).

    from os import path

    fib = None
    for libname in ('libfib.dll', 'libfib.so'):
        try:
            fib = ctypes.CDLL(path.join(path.curdir, libname))
        except OSError:
            pass
        else:
            break
    else:
        raise RuntimeError("Can't find the libfib library, "
                           "did you run the build script for your platform?")
    return fib



# If successful, this completes step 2.
fib = load_fib()
