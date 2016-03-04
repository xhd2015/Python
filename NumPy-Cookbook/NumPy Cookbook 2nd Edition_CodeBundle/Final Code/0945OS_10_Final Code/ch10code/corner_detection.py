from sklearn.datasets import load_sample_images
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import corner_harris
from skimage.feature import corner_peaks
from skimage.color import rgb2gray

dataset = load_sample_images()
img = dataset.images[0]
gray_img = rgb2gray(img)
harris_coords = corner_peaks(corner_harris(gray_img))
y, x = np.transpose(harris_coords)
plt.axis('off')
plt.imshow(img)
plt.plot(x, y, 'ro')
plt.show()
