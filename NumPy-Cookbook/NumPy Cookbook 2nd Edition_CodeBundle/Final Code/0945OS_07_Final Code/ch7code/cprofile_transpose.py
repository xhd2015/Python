import numpy as np
import cProfile

def transpose(n):
   random_values = np.random.random((n, n))
   return random_values.T

cProfile.run('transpose(1000)')
