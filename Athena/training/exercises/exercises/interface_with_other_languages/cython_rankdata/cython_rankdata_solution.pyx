import numpy as np
cimport numpy as np
cimport cython


@cython.boundscheck(False)
@cython.cdivision(True)
def rankdata(a):
    """
    Ranks the data, dealing with ties appropriately.

    Equal values are assigned a rank that is the average of the ranks that
    would have been otherwise assigned to all of the values within that set.
    Ranks begin at 1, not 0.

    Parameters
    ----------
    a : array_like
        This array is first flattened.

    Returns
    -------
    rankdata : ndarray
         An array of length equal to the size of `a`, containing rank scores.

    Examples
    --------
    >>> rankdata([0, 2, 2, 3])
    array([ 1. ,  2.5,  2.5,  4. ])

    """
    # Type declarations.   Note that these 'cdef' statements are the *only*
    # changes that we've made in the function!
    cdef unsigned int i, j, n, sumranks, dupcount
    cdef np.ndarray[np.int_t, ndim=1] ivec
    cdef np.ndarray[np.float64_t, ndim=1] svec
    cdef np.ndarray[np.float64_t, ndim=1] ranks
    cdef double averank

    # Convert the array to floating point, and flatten.
    a = np.ravel(np.asarray(a, dtype=np.float64))
    n = len(a)

    # Sort, in two steps: use argsort to get the sorted indices, and then
    # use fancy indexing to create the sorted array.
    ivec = np.argsort(a)
    svec = a[ivec]

    # Create the array of ranks, taking into account repeated values.
    sumranks = 0
    dupcount = 0
    ranks = np.zeros(n, float)
    for i in xrange(n):
        sumranks += i
        dupcount += 1
        if i == n - 1 or svec[i] != svec[i + 1]:
            averank = sumranks / float(dupcount) + 1
            for j in xrange(i - dupcount + 1, i + 1):
                ranks[ivec[j]] = averank
            sumranks = 0
            dupcount = 0
    return ranks
