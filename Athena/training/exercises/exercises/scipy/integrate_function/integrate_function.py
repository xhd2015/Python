""" 
Integrate a Function
--------------------

Integrate sin using scipy.integrate.quad.

Topics: SciPy's integration library, vectorization.

1. Use scipy.integrate.quad to integrate sin from 0 to pi/4.  
   Print out the result. Hint::
       
       from scipy import integrate
       >>> integrate.quad?

2. Integrate sin from 0 to x where x is a range of values from 0 to 2*pi.  
   Compare this to the exact solution, -cos(x) + cos(0), on a plot.  
   Also plot the error between the two. 
   
   Hint: Use vectorize so that integrate.quad works with arrays as inputs and
   produces arrays as outputs.  
   
See: :ref:`integrate-function-solution`.
"""
from numpy import linspace, vectorize, sin, cos, pi
from scipy import integrate
from matplotlib.pyplot import plot, legend, show, subplot, xlabel, ylabel, \
                              title

# A. integrate sin from 0->2pi

# B. Integrate sin from 0 to x where x is a range of
#    values from 0, 2*pi
x = linspace(0, 2*pi, 101)
