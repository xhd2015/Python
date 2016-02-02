Introduction
============

The vectorlib package is a simple implementation of
a 3D vector class.

Example
-------

The following Python session shows examples of the
use of the Vector class::

    >>> from vectorlib.vector import Vector
    >>> u = Vector(1, 2, 0.5)
    >>> print u
    Vector(x=1, y=2, z=0.5)
    >>> u.abs()
    2.29128784747792
    >>> v = Vector(0, 1, 2)
    >>> u.dot(v)
    3.0
    >>> u.angle(v)
    0.945250237728822

See the reference documentation for more details.
