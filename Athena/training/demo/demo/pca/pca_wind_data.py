"""
Demo of PCA implemented using numpy.linalg.svd.

(scipy.linalg.svd could also be used.  Or even more convenient
is to use the PCA class from scikits-learn.)
"""

import numpy as np
import matplotlib.pyplot as plt


np.set_printoptions(precision=3)

# Read the wind data, and drop the first three columns (dates)
x = np.loadtxt('wind.data')[:, 3:]

# Subtract the mean
xz = x - x.mean(axis=0)

# Compute the SVD
u, s, vt = np.linalg.svd(xz, full_matrices=False)

n = xz.shape[0]
var = (s ** 2) / n
print "Variances of principal components"
print var

relvar = var / var.sum()

print "Relative variances of principal components"
print relvar

# Project the data onto the first two components.
y = np.dot(xz, vt[:2].T)

# Make the scatter plot.
plt.plot(y[:, 0], y[:, 1], 'bo', alpha=0.15)
plt.axis('equal')
plt.show()
