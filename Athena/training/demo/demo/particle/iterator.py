""" Example to demonstrate creation of an iterator
    that iterates over its attributes
"""

class AttributeIterator(object):
    def __iter__(self):
        self._ind, self._keys = 0, []
        self._keys = self.__dict__.keys()
        self._keys.remove('_ind')
        self._keys.remove('_keys')
        return self
    def next(self):
        try:
            attr = self._keys[self._ind]
        except IndexError:
            raise StopIteration
        self._ind += 1
        return getattr(self, attr)
