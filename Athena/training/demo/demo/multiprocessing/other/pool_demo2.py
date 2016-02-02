"""
A simple example of using a multiprocessing Pool to implement an
"embarassingly parallel" computation.
"""

from math import ceil
from multiprocessing import Pool, cpu_count


def sum_range(rng):
    """Sum the integers from rng[0] up to but not including rng[1]."""
    low, high = rng
    sum = 0
    for k in range(low, high):
        sum += k
    return sum


if __name__ == "__main__":

    # Sum the integers from 1 to n.
    n = 1000000

    num_workers = cpu_count()

    # Do the sum in batches; each process will be given a range of
    # length work_size (except the last batch, which may be smaller).
    work_size = int(ceil(float(n) / num_workers))

    # 'ranges' is the list of intervals to be passed to sum_range(rng).
    # For example, if n=100 and work_size=30, ranges will be
    #   [(1, 31), (31, 61), (61, 91), (91, 101)]
    ranges = [(k, min(k + work_size, n+1)) for k in range(1, n+1, work_size)] 
    print "%d work tasks" % len(ranges)

    pool = Pool()
    sums = pool.map(sum_range, ranges)
    total = sum(sums)
    print "Computed sum:", total
    print "Formula:     ", ((n+1)*n)/2
