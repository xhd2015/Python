"""
A simple example of using a multiprocessing Pool to implement an
"embarassingly parallel" computation.

See pool_demo2.py for a fancier version.
"""

from multiprocessing import Pool

def sum_range(rng):
    """Sum the integers from rng[0] up to but not including rng[1]."""
    low, high = rng
    sum = 0
    for k in range(low, high):
        sum += k
    return sum


if __name__ == "__main__":
    args = [(1, 251), (251, 501)]
    pool = Pool()
    sums = pool.map(sum_range, args)
    total = sum(sums)
