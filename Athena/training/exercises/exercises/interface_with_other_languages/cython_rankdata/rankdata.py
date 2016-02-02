
"""
Cythonize rankdata
------------------

The function rankdata(a) is defined below.  (This is a slightly modified
version of the function scipy.stats.rankdata.)  Given an array `a`, this
function returns an array containing the "ranks" of the elements of `a`.
If there are no repeated values in `a`, this is simply the numerical order
of the elements when sorted, starting with 1.  For example::

    >>> rankdata([25, 15, 10, 20])
    array([ 4.,  2.,  1.,  3.]

If there are repeated elements (i.e. "ties"), then all the repeated elements
are assigned the average rank of the group.  For example, in the following,
the value 10 occurs at rank 1 and 2, so both are assigned the rank 1.5.
Similarly, the value 25 occurs at ranks 4, 5 and 6, so all are assigned the
rank 5.0:: 

    >>> rankdata([25, 15, 10, 25, 25, 30, 10])
    array([ 5. ,  3. ,  1.5,  5. ,  5. ,  7. ,  1.5])

The implementation involves a loop over the array `a`.  Such loops are
relatively slow in Python, so this is a good candidate for speeding up
the function by implementing it in Cython.  That is the assignment for
this exercise.

1. Copy this file to cython_rankdata.pyx.  The file setup.py is already
   configured to build this extension module, so you can run::

       python setup.py build_ext --inplace

   If there are no problems in cython_rankdata.pyx, this will create the
   extension module, which you can import in python.  With no changes to
   the python at all, you may still see a speed improvement in the Cython
   version.  For example::
   
    In [2]: from rankdata import rankdata  # Python version

    In [3]: from cython_rankdata import rankdata as cyrankdata  # Cython version

    In [4]: x = np.random.randint(80, size=150)  # Create some test data

    In [5]: %timeit rankdata(x)
    1000 loops, best of 3: 373 us per loop

    In [6]: %timeit cyrankdata(x)
    1000 loops, best of 3: 300 us per loop

2. Start modifying cython_rankdata.pyx to improve its performance.  Here's
   a first step: add the lines::
   
       cimport numpy as np
       import cython
   
   after the normal python import of numpy.  Then start adding appropriate
   type declarations to the function rankdata that let Cython generate
   efficient C code.  You shouldn't have to change the algorithm--most of the
   crucial changes will be type declarations!

3. As you modify cython_rankdata.pyx, run cython on it with the "-a" option,
   and inspect the HTML file.  Ideally, the for-loop should contain *no*
   yellow lines.

Here's the peformance comparison of the original python version and the
Cython solution in cython_rankdata_solution.pyx::

    In [1]: from rankdata import rankdata 

    In [2]: from cython_rankdata_solution import rankdata as cyrankdata

    In [3]: x = np.random.randint(80, size=150)

    In [4]: %timeit rankdata(x)
    1000 loops, best of 3: 397 us per loop

    In [5]: %timeit cyrankdata(x)
    100000 loops, best of 3: 18.4 us per loop

That's better than 20 times faster.

Reminders:

* The most efficient indexing of array occurs when the index variable is
  an unsigned integer.

* Cython provides function decorators to turn off certain safety checks.
  Two that are relevant here are::

      @cython.cdivision(True)
      @cython.boundscheck(False)


See :ref:`cython-rankdata-solution`.         
"""

import numpy as np


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
