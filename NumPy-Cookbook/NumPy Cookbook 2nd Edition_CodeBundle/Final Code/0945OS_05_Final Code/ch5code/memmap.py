import numpy as np
import matplotlib.pyplot as plt

N = 512
NSQUARES = 30

# Initialize
img = np.zeros((N, N), np.uint8)
centers = np.random.random_integers(0, N, size=(NSQUARES, 2))
radii = np.random.randint(0, N/9, size=NSQUARES)
colors = np.random.randint(100, 255, size=NSQUARES)

# Generate squares
for i in xrange(NSQUARES):
   xindices = range(centers[i][0] - radii[i], centers[i][0] + radii[i])
   xindices = np.clip(xindices, 0, N - 1)
   yindices = range(centers[i][1] - radii[i], centers[i][1] + radii[i])
   yindices = np.clip(yindices, 0, N - 1)

   if len(xindices) == 0 or len(yindices) == 0:
      continue

   coordinates = np.meshgrid(xindices, yindices)
   img[coordinates] = colors[i]

# Load into memory map
img.tofile('random_squares.raw')
img_memmap = np.memmap('random_squares.raw', shape=img.shape)

# Display image
plt.imshow(img_memmap)
plt.axis('off')
plt.show()
