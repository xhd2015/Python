from __future__ import print_function
import numpy as np
from scipy.misc import lena
import matplotlib.pyplot as plt


lena = lena()
random_mask = np.random.randint(0, 2, size=lena.shape)

plt.subplot(221)
plt.title("Original")
plt.imshow(lena)
plt.axis('off')

masked_array = np.ma.array(lena, mask=random_mask)
print(masked_array)

plt.subplot(222)
plt.title("Masked")
plt.imshow(masked_array)
plt.axis('off')

plt.subplot(223)
plt.title("Log")
plt.imshow(np.log(lena))
plt.axis('off')

plt.subplot(224)
plt.title("Log Masked")
plt.imshow(np.log(masked_array))
plt.axis('off')

plt.show()
