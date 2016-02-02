"""
Demonstrate the use scipy.optimize.leastsq to fit data to a curve.

(See scipy.optimize.curve_fit for a simpler way to do this.)
"""

from numpy.random import randn
from numpy import linspace, pi, exp, sin
from scipy.optimize import leastsq

from pylab import plot, legend, savefig


def func(x, A, a, f, phi):
    return A * exp(-a * sin(f * x + phi))


def errfunc(params, x, data):
    return func(x, *params) - data


# Make same data for the demonstration.
# ptrue holds the "true" parameters.
ptrue = [3, 2, 1, pi]
x = linspace(0, 2 * pi, 25)
true = func(x, *ptrue)
noisy = true + 0.3 * randn(len(x))

# p0 is the initial guess of the parameter values.
p0 = [1, 1, 1, 1]
pmin, ierr = leastsq(errfunc, p0, args=(x, noisy))

xx = linspace(0, 2 * pi, 100)
est = func(xx, *pmin)
true = func(xx, *ptrue)

plot(xx, true, 'r-', x, noisy,
     'ro', xx, est, 'b--', linewidth=2)
legend(['True', 'Samples', 'Estimated'])
savefig('fitted.png')
