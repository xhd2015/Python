"""This module defines the Vector class. """

from math import acos, sqrt


class Vector(object):

    def __init__(self, x, y, z):
        """ Constructor method.
        """
        self.x = x
        self.y = y
        self.z = z

    def dot(self, v):
        """Returns the dot product with Vector *v*."""
        d = self.x * v.x + self.y * v.y + self.z * v.z
        return d

    def abs(self):
        """Returns the magnitude of the vector."""
        m = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return m

    def __repr__(self):
        s = "Vector(x=%s, y=%s, z=%s)" % (self.x, self.y, self.z)
        return s


if __name__ == "__main__":
    v1 = Vector(2.0, 13.0, -1.0)
    print v1, " magnitude is", v1.abs()
    v2 = Vector(1.0, 2.0, 3.0)
    print "v1.dot(v2) =", v1.dot(v2)
