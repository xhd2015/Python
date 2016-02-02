from numpy import linspace, cos, sin
from pylab import figure, show, xlabel, ylabel
# The following import is necessary to enable 3D plots in matplotlib.
import mpl_toolkits.mplot3d

t = linspace(0, 30, 1000)
x = t * cos(t)
y = t * sin(t)
z = t

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z)
xlabel('x')
ylabel('y')
show()
