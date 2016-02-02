"""
This script is based on the example in the docstring for the function
scipy.interpolate.griddata.


The function griddata is a convenient wrapper for several interpolation
classes.  If you enter the following in ipython

    from scipy.interpolate import griddata
    griddata??

to view the source code, you'll see that, depending on the value of 'method'
and the shape of the input data, griddata uses either NearestNDInterpolator,
LinearNDInterpolator or CloughTocher2DInterpolator.  These can be used
directly, and the direct use is preferable if you will interpolate different
inputs while using the same data samples.  For example, instead of the
following

    grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')

we could import 'LinearNDInterpolator' from scipy.interpolate, and use

    lin = LinearNDInterpolator(points, values)
    grid_z1 = lin((grid_x, grid_y))

Then the object 'lin' could be reused to interpolate more (x, y) values.
"""

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt


# The test function
def func(x, y):
    z = x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
    return z


# Desired interpolation grid.
grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

# "Known" points.
nsamples = 500
points = np.random.rand(nsamples, 2)
values = func(points[:, 0], points[:, 1])

# Interpolate using different methods.
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

# Plot the results.
plt.subplot(2, 2, 1)
plt.imshow(func(grid_x, grid_y).T, extent=(0, 1, 0, 1), origin='lower')
plt.plot(points[:, 0], points[:, 1], 'k.', ms=1)
plt.title('Original')
plt.subplot(2, 2, 2)
plt.imshow(grid_z0.T, extent=(0, 1, 0, 1), origin='lower')
plt.title('Nearest')
plt.subplot(2, 2, 3)
plt.imshow(grid_z1.T, extent=(0, 1, 0, 1), origin='lower')
plt.title('Linear')
plt.subplot(2, 2, 4)
plt.imshow(grid_z2.T, extent=(0, 1, 0, 1), origin='lower')
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
plt.show()
