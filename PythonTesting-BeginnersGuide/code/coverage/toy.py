def global_function(x):
    r"""
    >>> global_function(5)
    6
    """
    return x + 1

class example_class:
    def __init__(self, param):
        self.param = param

    def timestwo(self):
        return self.param * 2

    def __repr__(self):
        return '<example param="%s">' % self.param

if __name__ == '__main__':
    import doctest
    doctest.testmod()
