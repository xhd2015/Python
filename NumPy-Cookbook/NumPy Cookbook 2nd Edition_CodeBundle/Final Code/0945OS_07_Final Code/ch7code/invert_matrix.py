import numpy as np

def invert(n):
   a = np.matrix(np.random.rand(n, n))
   return a.I

sizes = 2 ** np.arange(0, 12)

for n in sizes:
   invert(n)
