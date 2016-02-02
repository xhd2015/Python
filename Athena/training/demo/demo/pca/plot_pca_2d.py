"""
Create a plot of 2D data samples with principal components.

This script uses the PCA class from scikits-learn.
"""

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# Generate n samples, each a 2D vector sampled from a multivariate
# normal distribution.
n = 500
np.random.seed(123)
mu = np.array([10.0, 15.0])
sigma = np.array([[5.35, -2.],
                  [-2., 1.85]])
data = np.random.multivariate_normal(mu, sigma, n)

# Use PCA from sklearn to compute the principal components.
pca = PCA().fit(data)

v0 = pca.components_[0]
if v0[0] > 0.0:
    # The plot looks better (IMHO) if v0[0] is negative.
    v0 *= -1
sv0 = v0 * pca.explained_variance_[0]
v1 = pca.components_[1]
sv1 = v1 * pca.explained_variance_[1]

# Scatter plot of the data.
plt.plot(data[:, 0], data[:, 1], 'bo', alpha=0.25)

# Plot the principal components (relative to the mean).
mean = data.mean(axis=0)
plt.plot([mean[0], mean[0] + sv0[0]], [mean[1], mean[1] + sv0[1]],
            'r', linewidth=3.5)
plt.plot([mean[0], mean[0] + sv1[0]], [mean[1], mean[1] + sv1[1]],
            'r', linewidth=3.5)

plt.axis('equal')
plt.grid(True)
plt.show()
