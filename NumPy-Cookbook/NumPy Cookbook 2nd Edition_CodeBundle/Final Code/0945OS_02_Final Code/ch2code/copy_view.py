import scipy.misc
import matplotlib.pyplot as plt

lena = scipy.misc.lena()
acopy = lena.copy()
aview = lena.view()

# Plot the Lena array
plt.subplot(221)
plt.imshow(lena)

#Plot the copy
plt.subplot(222)
plt.imshow(acopy)

#Plot the view
plt.subplot(223)
plt.imshow(aview)

# Plot the view after changes
aview.flat = 0
plt.subplot(224)
plt.imshow(aview)

plt.show()
