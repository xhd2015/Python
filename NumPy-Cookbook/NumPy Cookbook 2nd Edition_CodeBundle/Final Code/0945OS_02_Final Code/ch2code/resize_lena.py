import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

# This script resizes the Lena image from Scipy.

# Loads the Lena image into an array
lena = scipy.misc.lena()

#Lena's dimensions
LENA_X = 512
LENA_Y = 512

#Check the shape of the Lena array
np.testing.assert_equal((LENA_X, LENA_Y), lena.shape)

# Set the resize factors
yfactor = 2
xfactor = 3

# Resize the Lena array
resized = lena.repeat(yfactor, axis=0).repeat(xfactor, axis=1)

#Check the shape of the resized array
np.testing.assert_equal((yfactor * LENA_Y, xfactor * LENA_Y), resized.shape)

# Plot the Lena array
plt.subplot(211)
plt.title("Lena")
plt.axis("off")
plt.imshow(lena)

#Plot the resized array
plt.subplot(212)
plt.title("Resized")
plt.axis("off")
plt.imshow(resized)
plt.show()
