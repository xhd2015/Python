from numpy import pi, sin, r_, vectorize
import pylab as plt

# special.sinc already available
# This is just for show.
def sinc(x): 
    if x == 0.0:
        return 1.0
    else:
        w = pi*x
        return sin(w) / w

try:
    sinc([1.3,1.5])
except TypeError:
    print "sinc: doesn't work with sequences.  Must vectorize!"

# vectorize the sinc function so that it can be called with arrays.
vsinc = vectorize(sinc)        
x = r_[-5:5:100j]
y = vsinc(x)
plt.plot(x, y)
plt.show()
