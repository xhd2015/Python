#############################################################################
# array_1.py
#
# 1. Use an event to externally manage updates.
#############################################################################

# Major imports
import numpy

# enthought imports
from traits.api import HasTraits, Array


class TriangleMesh(HasTraits):
    """ Represent a triangular surface mesh with a list of points
        and a secondary array that defines the connectivity of these
        points (ie. triangles).
    """

    # An Nx3 floating point array of points (vertices) within the mesh.
    points = Array(dtype=numpy.float32, shape=(None,3))

    # An Mx3 integer array of indices into the points array.
    # Each row defines a triangle in the mesh.
    triangles = Array(dtype=numpy.int32, shape=(None,3))

# Demo Code
points = numpy.array([[0,0,0],
                      [1,0,0],
                      [0,1,0],
                      [0,0,1]], dtype=numpy.float32)

triangles = numpy.array([[0,1,3],
                         [0,3,2],
                         [1,2,3],
                         [0,2,1]], dtype=numpy.int32)

# Create a TriangleMesh
tetra = TriangleMesh()

# Set the data points and connectivity
tetra.points = points
tetra.triangles = triangles

# print out the points
print tetra.points

print "THIS WILL RAISE AN EXCEPTION"
tetra.points = points[:,:2]
