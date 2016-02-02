"""
Code Check
----------

This code has an assortment of bugs, and its style doesn't
conform to PEP-8.  Use pyflakes and pep8 to find and fix
the code.

You may have to install pep8 with the command:

$ easy_install pep8

It might take a few iterations before pyflakes doesn't
complain about something.

See: :ref:`code-check-solution`.
"""
from math import asin, acos

class Vector(object):  
    
    def __init__(self, x, y):
        """ Constructor method.
        """
        self.x = x
        self.y = y
        self.z = z

    def dot(self, v):
        d = self.x * v.x + self.y * v.y +self.z * v.z
        return d

    def abs(self):
        m = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return m

    def angle(self, v):
        theta = acos(self.dot(v) / (self.abs() * v.abs()))

    def __repr__(self)
       s = "Vector(x=%s, y=%s, z=%s)" % (self.x, self.y, slef.z)
       return s


if __name__ == "__main__":
    v1 = Vector(2.0,13.0, -1.0)
    print v1, " magnitude is", v1.abs()
    v2 = Vector(1.0, 2.0, 3.0)
    print "v1.angle(v2) =", v1.angle(v2)