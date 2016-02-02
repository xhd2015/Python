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
               
"""
import time

from numpy import linspace, mgrid, abs, amin, amax
from scipy import special

from matplotlib.pyplot import plot, grid, title, figure, subplot, imshow, show,\
                  colorbar, legend 

# 1. Plot the erf function (special.erf) for real values -5 to 5.
x = linspace(-5,5,101)
y = special.erf(x)

figure()
plot(x, y)
grid()
title("Error Function (Erf)")

# 2. Calculate the error function on the imaginary plane
# with the both the real and imaginary parts ranging 
# from -1 to 1.

imag_part, real_part = mgrid[-1:1:51j, -1:1:51j]
complex_plane = real_part + imag_part * 1j
result = special.erf(complex_plane)

# Find the dynamic range of the values we want to display so that
# they can share the same scale.
min_color_range = min(amin(result.real), amin(result.imag), amin(abs(result)))
max_color_range = max(amax(result.real), amax(result.imag), amax(abs(result)))


figure()
subplot(1,3,1)
imshow(result.real, vmin=min_color_range, vmax=max_color_range,
       extent=[-1,1,-1,1])
title("Real part of erf")
subplot(1,3,2)
imshow(result.imag, vmin=min_color_range, vmax=max_color_range,
       extent=[-1,1,-1,1])
title("imaginary part of erf")
subplot(1,3,3)
imshow(abs(result), vmin=min_color_range, vmax=max_color_range,
       extent=[-1,1,-1,1])
colorbar()
title("Magnitude of erf")
    

# 3. Plot the 0th through 4th order bessel functions over the
#    range 0 to 10.  Use special.jn
figure()
x = linspace(0,10,101)
for i in range(5):
    y = special.jn(i, x)
    plot(x, y, label="J%d" % i)
grid()
legend()
title("Family of Bessel Functions")               

show()

# 4. Time j0 vs. jn for a million element array.
x = linspace(0,10,1e6)

t1 = time.time()
y = special.j0(x)
t2 = time.time()
print "j0:", t2 - t1  

t1 = time.time()
y = special.jn(0, x)
t2 = time.time()
print "jn:", t2 - t1
