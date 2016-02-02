
from numpy import linspace, sin, cos, meshgrid

from pylab import figure, show, xlabel, ylabel
from matplotlib import cm
# The following import is necessary to enable 3D plots in matplotlib.
from mpl_toolkits.mplot3d import Axes3D

n = 35
x = linspace(-5, 5, n)
y = linspace(0, 10, n)
X, Y = meshgrid(x, y)
Z = X * sin(X) * cos(0.25 * Y)

fig = figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.copper)
xlabel('x')
ylabel('y')
show()
