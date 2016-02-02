import numpy as np
from mayavi import mlab
from mayavi.mlab import pipeline
from scipy.interpolate import Rbf

# Local import
from datagen import synth_cube

# ----------------------------------------------------------------------
# Part 0 - the data cube.

# Get a cube of data for demonstration.
n = 160
data = synth_cube(n)

# ----------------------------------------------------------------------
# Part 1 -- "image plane widgets"

field = pipeline.scalar_field(data)

pipeline.image_plane_widget(field, plane_orientation='x_axes', colormap='RdBu')
pipeline.image_plane_widget(field, plane_orientation='y_axes', colormap='RdBu')
pipeline.image_plane_widget(field, plane_orientation='z_axes', colormap='RdBu')

mlab.outline(color=(1, 1, 1))

# ----------------------------------------------------------------------
# Part 2 - contour surface

c = pipeline.contour_surface(field, opacity=0.5, contours=3, colormap='RdBu')
# Initially hide it.
##c.visible = False

# ----------------------------------------------------------------------
# Part 3 - add a pipe.

# Generate a curve inside the cube.
x = np.linspace(data.shape[0] / 3, data.shape[0], 10)
y = x - 3 + ((x - 3) / 35.) ** 2
z = 100 * np.sin((x - x[0]) / 50)

c = mlab.plot3d(x, y, z, tube_radius=5, color=(1, 1, 0))
##c.visible = False

# ----------------------------------------------------------------------
# Part 4 - add surface

# Create a surface
x, y = np.ogrid[:n:4, :n:4]
z = 80 + (0.15 * (-x - 0.015 * x ** 2 + 0.3 * y + 0.01 * y ** 2)).astype(int)

s = mlab.surf(x, y, z, representation='surface', colormap='summer')
# Initially hide the surface.
##s.visible = False

# ----------------------------------------------------------------------
# Part 5 - Evaluate the data cube on the surface, and plot it.

# Do a simple linear interpolation to evaluate the data cube on the
# surface.
low_index = np.floor(z).astype(int)
hi_index = np.ceil(z).astype(int)
low_vals = data[x, y, low_index]
hi_vals = data[x, y, hi_index]
vals = low_vals + (z - low_index) * (hi_vals - low_vals)

# Make what is effectively a 2D image plot in another figure.
mlab.figure()
mlab.imshow(x, y, vals, colormap='RdBu')
