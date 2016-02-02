"""
Mandelbrot with Weave
---------------------

The code in this script generates a plot of the Mandelbrot set.

1. Use weave to speed up this code 
2. Compare the speed of the weave code with the NumPy-only version. 

Hints:
* The mandelbrot_escape function should be placed in support_code and 
weave.inline should be used to inline a 2-d loop over the data passed in
* The output data should be pre-allocated and passed in as another array. 
* Recall that weave creates C++ extensions so that std::

   complex<double>

can be used.

See :ref:`mandelbrot-weave-solution`.
"""

import time

from numpy import vectorize, r_, c_
from matplotlib.pyplot import imshow, show, cm

def mandelbrot_escape(c):
    """ Compute escape time for points near the Mandelbrot set.
    
    This computes the number of iterations required for the sequence
    
    .. math::
    
        z_{n+1} = z_n^2 + c
    
    to repeat before |z_n| > 2 (which implies that the sequence diverges to
    infinity).  If we iterate 1000 times without the absolute value getting
    large, then we consider the point to be in the Mandelbrot set, and return
    the value -1.
    
    Parameters
    ----------
    
    c : complex
        The point on the complex plane being tested.
    
    Returns
    -------
    
    i : int
        The escape time for the point, or -1 if the point never escaped.
    """
    z = c
    for i in range(1000):
        z = z**2 + c
        if abs(z) >= 2:
            break
    else:
        i = -1
    return i

# vectorize the function so we can apply it to a complex array
vmand = vectorize(mandelbrot_escape)

# set up the grid of points to test
x = r_[-2:1:500j]
y = c_[-1.5:1.5:500j]
z = x + y*1j

# compute the escape times, and how long it takes to run the code
t = time.time()
d = vmand(z)
print 'Execution time:', time.time() - t

# plot the Mandelbrot set
imshow(d, cmap=cm.gist_stern)
show()
