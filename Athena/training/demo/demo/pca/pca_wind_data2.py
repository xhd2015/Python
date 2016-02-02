"""
Demo of PCA using the class sklearn.decomposition.PCA.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

np.set_printoptions(precision=3)

# Read the wind data, and drop the first three columns (dates)
x = np.loadtxt('wind.data')[:, 3:]

pca = PCA().fit(x)

print "Variances of principal components"
print pca.explained_variance_

print "Relative variances of principal components"
print pca.explained_variance_ratio_

pca2 = PCA(n_components=2).fit(x)
x2 = pca2.fit_transform(x)

# Make the scatter plot.
plt.plot(x2[:, 0], x2[:, 1], 'ro', alpha=0.15)
plt.axis('equal')
plt.show()
