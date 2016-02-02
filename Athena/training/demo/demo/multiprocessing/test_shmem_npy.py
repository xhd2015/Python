import multiprocessing as mp
from multiprocessing import sharedctypes
from numpy import ctypeslib
import numpy as np

def worker(raw_arr, (lower, upper), n, fill):
    arr = ctypeslib.as_array(raw_arr)
    arr.shape = (n, n)
    arr = arr[lower:upper, :]
    arr.fill(fill)

if __name__ == '__main__':
    n = 128
    nprocs = 4
    ra = sharedctypes.RawArray('d', n * n)
    breaks = np.arange(0, n+1, n/nprocs)
    slices = [(lower, upper) for lower, upper in zip(breaks[:-1], breaks[1:])]
    args = [(ra, slice, n, i) for i, slice in enumerate(slices)]
    ps = [mp.Process(target=worker, args=arg) for arg in args]
    [p.start() for p in ps]
    [p.join() for p in ps]
    g_arr = ctypeslib.as_array(ra)
    g_arr.shape = (n, n)
    import pylab
    pylab.imshow(g_arr)
    pylab.show()
