""" 
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
"""
from numpy import linspace, vectorize, sin, cos, pi
from scipy import integrate
from matplotlib.pyplot import plot, legend, show, subplot, xlabel, ylabel, \
                              title

# A. integrate sin from 0->pi/2
result, error = integrate.quad(sin,0, pi/2)
print "integral(sin 0->pi/2):", result

# B. Integrate sin from 0 to x where x is a range of
#    values from 0, 2*pi

x = linspace(0, 2*pi, 101)

# 1. quad needs to be vectorized before you can call it with an array.
vquad = vectorize(integrate.quad)

# 2. Now calculate the integral using the vectorized function. 
approx, error_est = vquad(sin, 0, x)

# 3. Evaluate the actual integral value for x.
exact = -cos(x) + cos(0)

# 4. Plot the comparison.
subplot(1,2,1)
plot(x, approx, label="Approx")
plot(x, exact, label="Exact")
xlabel('x')
ylabel('integral(sin)')
title('Integral of sin from 0 to x')
legend()

subplot(1,2,2)
plot(x, exact-approx)
title('Error in approximation')
show()