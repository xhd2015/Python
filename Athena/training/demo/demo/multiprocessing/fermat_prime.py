import multiprocessing as mp
from random import randrange
from time import time
import numpy as np

def fermat_prime(p, k=100):
    for _ in range(k):
        a = randrange(1, p)
        if pow(a, p-1, p) != 1:
            return (False, p)
    return (True, p)

def profile():
    '''
    Runs the fermat_prime() function with different sized pools and gathers
    timing information into a scaling plot.
    '''
    res = []
    for nprocs in range(1, 10):
        pl = mp.Pool(processes=nprocs) # creates a pool of `cpu_count()` processes.
        n0, n1 = 10, 10000
        t0 = time()
        pl.map(fermat_prime, range(n0, n1))
        t0 = time() - t0
        num_per_sec = (n1 - n0) / t0
        res.append((nprocs, num_per_sec))
    import pylab as pl
    x, y = zip(*res)
    x = np.array(x)
    y = np.array(y)
    y = y / y[0]
    y0 = y[0]
    linear_scaling = y0 * np.array(x)
    pl.plot(x, y, 'ro', label='actual')
    pl.plot(x, linear_scaling, 'b-', label='linear scaling')
    pl.legend()
    pl.ylabel('Speedup')
    pl.xlabel('Number of processors')
    pl.title('Scaling of Pool.map() prime computation on an 8 Core i7')
    pl.grid()
    pl.show()

def main():
    pl = mp.Pool() # creates a pool of `cpu_count()` processes.
    p_to_nums = pl.map(fermat_prime, range(50, 100))
    for isp, num in p_to_nums:
        if isp: print num, "is prime"

if __name__ == '__main__':

    main()
    # profile()
