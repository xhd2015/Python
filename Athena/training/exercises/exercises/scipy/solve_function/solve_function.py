
""" 
Using fsolve
------------

1. Define a function `funcv(x)` that computes the following
    
       f0 = x0**2 + x1**2 - 2.0
       f1 = x0**2 - x1**2 - 1.0

    where x0 = x[0] and x1 = x[1], and the return value of
    funcv(x) is (f0, f1).

2. Find x0 and x1 so that f0==0 and f1==0.
   Hint: See scipy.optimize.fsolve.

3. Create images of f0 and f1 around 0 and
   plot the guess point and the solution point.        
   
See :ref:`solve-function-solution`.
"""

# Numeric library imports
from numpy import array, ogrid
from scipy import optimize

# Plotting functions
from matplotlib.pyplot import subplot, imshow, hold, figure, clf, plot, \
                    colorbar, title, show
                    
# 1. Define the function.


# 2. Solve the system of equations. 

# Set a starting point for the solver and then find x_opt

print 'optimal x:', x_opt
print 'optimal f(x):', funcv(x_opt)


# 3. Plot the results and the guess: 

# Make some pretty plots to show the function space as well
# as the solver starting point and the solution.

# Create 2D arrays x and y and evaluate them so that we 
# can get the results for f0 and f1 in the system of equations.
x,y = ogrid[-6:6:100j,-6:6:100j]
f0, f1 = funcv([x,y])

# Set up a plot of f0 and f1 vs. x and y and show the 
# starting and ending point of the solver on each plot.

