
# Demonstrate the use of __getstate__() and __setstate__().


from cPickle import dumps, loads
import numpy as np


class Foo(object):

    # This class does not define __getstate__(), so when an instance
    # is pickled, all the attributes (x, y, and z) are saved.
    # (Note: a better implementation of this class might make z a
    # *property*; see the Python documentation for details.)

    def __init__(self, x, y):
        """x and y must be 1D numpy arrays."""
        self.x = x
        self.y = y
        self.compute_z()

    def compute_z(self):
        """
        Compute sin(x*y) on the grid whose x and y coordinates
        are self.x and self.y.  Save the result in self.z.
        """
        X, Y = np.meshgrid(self.x, self.y)
        self.z = np.sin(X*Y)


class Bar(Foo):

    # In this subclass of Foo, we define __getstate__() and __setstate_().
    # __getstate__() returns a tuple containing just self.x and self.y; this
    # is the data that will be pickled.  When unpickled, __setstate__() is
    # called with this object.  __setstate__() will restore the attributes
    # self.x and self.y, and call self.compute_z() to recompute z.

    def __getstate__(self):
        # Return a tuple containing just self.x and self.y.
        # We intentionally do not include self.z in the state.
        return self.x, self.y

    def __setstate__(self, xy):
        self.x, self.y = xy
        self.compute_z()


if __name__ == "__main__":
    x = np.linspace(0, 1, 11)
    y = np.linspace(0, np.pi, 15)

    # Create and pickle instances of Foo and Bar.

    f1 = Foo(x, y)
    sf1 = dumps(f1)
    print "len(sf1) =", len(sf1)

    b1 = Bar(x, y)
    sb1 = dumps(b1)
    print "len(sb1) =", len(sb1)

    # Unpickle the instances, and verify that z is the same in both.

    f2 = loads(sf1)
    b2 = loads(sb1)
    print "f2.z = b2.z:", np.all(f2.z == b2.z)
