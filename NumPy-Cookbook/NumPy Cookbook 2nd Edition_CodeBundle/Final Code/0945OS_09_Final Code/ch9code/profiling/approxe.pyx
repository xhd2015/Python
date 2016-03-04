def approx_e(int n=40, display=False):
    cdef double sum = 0.
    cdef double factorial = 1.
    cdef int k

    for k in xrange(1,n+1):
        factorial *= k
        sum += 1/factorial

    if display:
        print(1 + sum)

