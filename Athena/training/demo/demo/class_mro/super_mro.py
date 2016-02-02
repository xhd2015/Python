class A(object):
    def __init__(self, arg):
        print "A"
        super(A, self).__init__()

class B(object):
    def __init__(self, arg):
        print "B"
        super(B, self).__init__()

class C(A):
    def __init__(self, arg):
        print "C","arg=",arg
        super(C, self).__init__(arg)

class D(B):
    def __init__(self, arg):
        print "D", "arg=",arg
        super(D, self).__init__(arg)

class E(C,D):
    def __init__(self, arg):
        print "E", "arg=",arg
        super(D, self).__init__(arg)

print "MRO:", [x.__name__ for x in E.__mro__]
E(10)
