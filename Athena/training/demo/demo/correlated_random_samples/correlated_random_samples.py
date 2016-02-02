"""Generate correlated random samples using numpy.

This script provides a basic demo of how to generate
correlated random samples using the function
numpy.random.multivariate_normal.

"""

import numpy as np
from numpy.random import multivariate_normal

from pylab import plot, axis, grid, show, xlabel, ylabel


# Desired means and covariance matrix.
mu = np.array([0.0, 2.0])
s = np.array([[2.7, -1.5], [-1.5, 1.8]])

# Number of samples to generate.
n = 2500

# Correlated samples.
y = multivariate_normal(mu, s, size=n).T

# Print the covariance of the samples.
print np.cov(y)

plot(y[0], y[1], 'bo')
axis('equal')
grid(True)
xlabel('y[0]')
ylabel('y[1]')
show()
