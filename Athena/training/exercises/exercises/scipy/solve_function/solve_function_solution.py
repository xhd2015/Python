
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
   
"""

# Numeric library imports
from numpy import array, ogrid
from scipy import optimize

# Plotting functions
from matplotlib.pyplot import subplot, imshow, hold, figure, clf, plot, \
                    colorbar, title, show

# 1. Define the function.

def funcv(x):
    """ System of equations to solve for. The input x has 2 elements, 
        and the function returns two results.
    """
    f0 = x[0]**2 + x[1]**2 - 2.0
    f1 = x[0]**2 - x[1]**2 - 1.0
    return f0, f1

# 2. Solve the system of equations. 

# Set a starting point for the solver
x_guess = array([4, 4])

# Solve the equation using fsolve
# x_guess is changed in place, so were going to make a copy...

x_opt = optimize.fsolve(funcv, x_guess.copy())
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
figure(1)
clf()
subplot(1,2,1)
imshow(f0, extent=(-6, 6, -6, 6), vmin=-20, vmax=50)
hold(True)
plot([x_guess[0]], [x_guess[1]], 'go')
plot([x_opt[0]], [x_opt[1]], 'ro')
colorbar()
title(r'$f_0$')


subplot(1,2,2)
imshow(f1, extent=(-6, 6, -6, 6), vmin=-20, vmax=50)
hold(True)
plot([x_guess[0]], [x_guess[1]], 'go')
plot([x_opt[0]], [x_opt[1]], 'ro')
colorbar()
title(r'$f_1$')

show()
