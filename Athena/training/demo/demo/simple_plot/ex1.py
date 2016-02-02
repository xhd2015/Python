from numpy import arange, array, pi, sin
from pylab import plot, show

x = arange(101.)

# multiply entire array by 
# scalar value
a = (2*pi)/100.

# apply functions to array.
y = sin(a*x)
plot(x,y)
show()

