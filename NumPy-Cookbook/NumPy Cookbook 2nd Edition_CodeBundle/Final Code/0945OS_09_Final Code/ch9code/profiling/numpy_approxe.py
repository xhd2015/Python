from __future__ import print_function
import numpy as np
import cProfile
import pstats

def approx_e(n=40, display=False):
   # array of [1, 2, ... n-1]
   arr = np.arange(1, n) 

   # calculate the factorials and convert to floats
   arr = arr.cumprod().astype(float)

   # reciprocal 1/n
   arr = np.reciprocal(arr)

   if display:
    print(1 + arr.sum())

# Repeat multiple times because NumPy is so fast
def run(repeat=2000):
    for i in range(repeat):
        approx_e()


cProfile.runctx("run()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()

approx_e(display=True)

