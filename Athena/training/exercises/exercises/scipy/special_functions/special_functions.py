""" 
Working with Special Functions
------------------------------

1. Import the special function library from scipy, and
   look at its docstring to see a summary of the functions
   it provides. To do this in IPython, type the following::
   
        In [1]: from scipy import special
        In [2]: special?<return>
      
2. Plot the error function (special.erf) for real values -5 to 5.
   Use the grid() and title() functions from pylab to spruce-up
   your plot.
   
3. Now calculate the error function on the imaginary plane
   with the both the real and imaginary parts ranging 
   from -1 to 1.  Use subplot and imshow to show:
          
      a) the real part of erf.
      b) the imaginary part of erf.
      c) the magnitude of erf.

   Use the "extent" keyword argument for imshow to set up the
   axis scales correctly.
   
   [Hint: mgrid is helpful for creating the input for this.]

4. Plot the 0th through 4th order bessel functions over the
   range 0 to 10.  Use special.jn.
   
5. The "special" library has some "specialized" functions for
   quickly calculating specific versions of general functions.
   For example, the function special.jn(0, x) calculates the
   zeroth order bessel function.  So does special.j0(x).  
   
   Create a large x array (linspace(0, 10, 1e6), and compare the
   speed of j0 to jn for the zeroth order bessel function.
   On Windows, a common way to time a function is as follows::
   
       import time
       t1 = time.time()
       <your code>
       t2 = time.time()
       print "run time:", t2 - t1
   
   If you are on Unix, use time.clock() instead.
   
See :ref:`special-functions-solution`.
               
"""
import time

from numpy import linspace, mgrid, abs, amin, amax
from scipy import special

from matplotlib.pyplot import plot, grid, title, figure, subplot, imshow, show,\
                  colorbar, legend 

# 1. Plot the erf function (special.erf) for real values -5 to 5.
x = linspace(-5,5,101)

# 2. Calculate the error function on the imaginary plane
# with the both the real and imaginary parts ranging 
# from -1 to 1.

    

# 3. Plot the 0th through 4th order bessel functions over the
#    range 0 to 10.  Use special.jn

# 4. Time j0 vs. jn for a million element array.
