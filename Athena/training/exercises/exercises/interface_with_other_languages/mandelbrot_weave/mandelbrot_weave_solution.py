"""
Mandelbrot with Weave
---------------------

The code in this script generates a plot of the Mandelbrot set.

1) Use weave to speed up this code 
2) Compare the speed of the weave code with the vectorized-only version. 

Hints:  * The mandelbrot_escape function should be placed in support_code and
             weave.inline should be used to inline a 2-d loop over the data passed in
        * The output data should be pre-allocated and passed in as another array. 
        * Recall that weave creates C++ extensions so that std::complex<double> can
             be used.
"""

import time

from numpy import r_, empty, intc, vectorize, newaxis
from matplotlib.pyplot import imshow, show, cm, figure
from scipy import weave

support_code = """

static int mandelbrot_escape(std::complex<double> c) {
    std::complex<double> z;
    int i;
    z = c;
    for (i=0; i<1000; i++) {
        z = z*z + c;
        if (std::abs(z) >= 2) break;
    }
    if (i==1000) i=-1;
    return i;   
}
"""

code = """
int i,j;
std::complex<double> z;
for (i=0; i<Ny[0]; i++) {
    for (j=0; j<Nx[0]; j++) {
        z = std::complex<double>(X1(j), Y1(i));
        D2(i,j) = mandelbrot_escape(z);
    }
}
"""

# set up the grid of values
x = r_[-2:1:500j]
y = r_[-1.5:1.5:500j]

# compute the escape time values
start = time.time()
d = empty((x.size, y.size), intc)
weave.inline(code, ['x', 'y', 'd'], support_code = support_code)
print "Weave: ", time.time() - start

# plot the Mandelbrot set
figure(1)
imshow(d, cmap=cm.gist_stern)
show()

# Vectorize solution

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

start = time.time()
z = x + y[:,newaxis]*1j
d2 = vmand(z)
print "Vectorize: ", time.time() - start

figure(2)
imshow(d2, cmap=cm.gist_stern)

show()
