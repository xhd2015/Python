""" 
Data Fitting
------------

1. Define a function with four arguments, x, a, b, and c, that computes::
   
       y = a*exp(-b*x) + c

   (This is done for you in the code below.)
    
   Then create an array x of 75 evenly spaced values in the interval
   0 <= x <= 5, and an array y = f(x,a,b,c) with a=2.0, b = 0.76, c=0.1.

2. Now use scipy.stats.norm to create a noisy signal by adding Gaussian
   noise with mean 0.0 and standard deviation 0.2 to y.

3. Calculate 1st, 2nd and 3rd degree polynomial functions to fit to the data.
   Use the polyfit and poly1d functions from scipy.

4. Do a least squares fit to the original exponential function using 
   scipy.curve_fit.

See: :ref:`data-fitting-solution`.
"""

from matplotlib.pyplot import plot, title, show, hold, legend, subplot
from numpy import exp, linspace
from scipy import polyfit, poly1d
from scipy.stats import norm
from scipy.optimize import curve_fit

# 1. Define the function and create the signal.

def function(x, a, b, c):
    y = a*exp(-b*x) + c
    return y

a = 2.0
b = 0.76
c = 0.1
