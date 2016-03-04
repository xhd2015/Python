import numpy as np
import time

@profile
def multiply(n):
   A = np.random.rand(n, n)
   time.sleep(np.random.randint(0, 2))
   return np.matrix(A) ** 2

for n in 2 ** np.arange(0, 10):
   multiply(n)


