# Use dumps() to pickle a class instance, and loads() to unpickle it.
# Demonstrate that a class attribute is not saved in the pickle.

from cPickle import dumps, loads


class Foo(object):

    # 'group' is a class attribute; this value is *not* saved in a
    # pickled instance.
    group = 0

    def __init__(self, ratio):
        # 'ratio' is an instance attribute.  This is saved when
        # an instance is pickled.
        self.ratio = ratio

    def __str__(self):
        s = "Foo: group=%s, ratio=%s" % (self.group, self.ratio)
        return s


if __name__ == "__main__":
    f1 = Foo(1.5)
    print "f1 =", f1   # f1 = Foo: group=0, ratio=1.5

    s = dumps(f1)

    # Change the class attribute Foo.group:
    Foo.group = -1

    # Unpickle s to f2, and see what we get:
    f2 = loads(s)
    print "f2 =", f2   # f1 = Foo: group=-1, ratio=1.5
