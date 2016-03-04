import numpy as np
import matplotlib.pyplot as plt
from random import choice
import scipy
import scipy.ndimage

# Initialization
NFIGURES = 5
k = np.random.random_integers(1, 5, NFIGURES)
a = np.random.random_integers(1, 5, NFIGURES)

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

lena = scipy.misc.lena()
plt.subplot(211)
plt.imshow(lena)
plt.axis('off')

# Blur Lena
plt.subplot(212)
blurred = scipy.ndimage.gaussian_filter(lena, sigma=4)

plt.imshow(blurred)
plt.axis('off')

# Plot in polar coordinates
theta = np.linspace(0, k[0] * np.pi, 200)
plt.polar(theta, np.sqrt(theta), choice(colors))

for i in xrange(1, NFIGURES):
   theta = np.linspace(0, k[i] * np.pi, 200)
   plt.polar(theta, a[i] * np.cos(k[i] * theta), choice(colors))

plt.axis('off')

plt.show()
