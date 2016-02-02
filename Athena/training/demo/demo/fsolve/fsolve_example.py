""" fsolve example.

    API docs here (scipy version 0.10.1):
        http://docs.scipy.org/doc/scipy-0.10.1/reference/optimize.html
"""

# Numeric library imports
from numpy import array, mgrid
from scipy import optimize

# Plotting functions
from matplotlib import pylab


def funcv(x):
    """ System of equations to solve for. The input x has 2 elements,
        and the function returns two results.
    """
    f0 = x[0] ** 3.0 + x[1] + 3.0
    f1 = x[1] - 4.0 * x[0]
    return f0, f1


# Set a starting point for the solver
x_guess = array((50.0, 10.0))

# Solve the equation using fsolve
# x_guess is changed in place, so were going to make a copy...
x_opt = optimize.fsolve(funcv, x_guess.copy())
print 'optimal x:', x_opt
print 'optimal f(x):', funcv(x_opt)

# Make some pretty plots to show the function space as well
# as the solver starting point and the solution.

# Create 2D arrays x and y and evaluate them so that we
# can get the results for f0 and f1 in the system of equations.
x, y = mgrid[-100:100:.5, -100:100:.5]
f0, f1 = funcv((x, y))

# Set up a plot of f0 and f1 vs. x and y and show the
# starting and ending point of the solver on each plot.
pylab.figure(figsize=(14, 5))
pylab.subplot(1, 2, 1)
pylab.imshow(f0, extent=(-100, 100, -100, 100), cmap=pylab.cm.coolwarm)
pylab.hold(True)
pylab.plot([x_guess[0]], [x_guess[1]], 'go')
pylab.plot([x_opt[0]], [x_opt[1]], 'ro')
pylab.colorbar()

pylab.subplot(1, 2, 2)
pylab.imshow(f1, extent=(-100, 100, -100, 100), cmap=pylab.cm.coolwarm)
pylab.hold(True)
pylab.plot([x_guess[0]], [x_guess[1]], 'go')
pylab.plot([x_opt[0]], [x_opt[1]], 'ro')
pylab.colorbar()

pylab.show()
