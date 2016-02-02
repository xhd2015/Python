from numpy import linspace, pi, sin
from scipy.interpolate import Rbf
from pylab import plot, axis, legend, show

# sample values
x = linspace(0,2*pi,6)
y = sin(x)

# Create a spline class for interpolation.
fit = Rbf(x,y,function='gaussian')
xx = linspace(0,2*pi, 50)
yy = fit(xx)

# display the results.
plot(xx, sin(xx), 'r--', x,y,'ro',xx,yy, 'b-',linewidth=2)
axis('tight')
legend(['actual sin', 'original samples', 'interpolated curve'])
show()
