import scipy.misc
import matplotlib.pyplot as plt

# Load the Lena array
lena = scipy.misc.lena()

# Plot the Lena array
plt.subplot(221)
plt.title('Original')
plt.axis('off')
plt.imshow(lena)

#Plot the flipped array
plt.subplot(222)
plt.title('Flipped')
plt.axis('off')
plt.imshow(lena[:,::-1])

#Plot a slice array
plt.subplot(223)
plt.title('Sliced')
plt.axis('off')
plt.imshow(lena[:lena.shape[0]/2,:lena.shape[1]/2])

# Apply a mask
mask = lena % 2 == 0
masked_lena = lena.copy()
masked_lena[mask] = 0
plt.subplot(224)
plt.title('Masked')
plt.axis('off')
plt.imshow(masked_lena)

plt.show()
