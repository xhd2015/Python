from inspect import *

def print_doc(name, item):
    if item.__doc__:
        print "Documentation for %s" % name
        print "-------------------------------"
        print item.__doc__
        print "-------------------------------"
    else:
        print "Documentation for %s - None" % name

def print_docstrings(m, prefix=""):
    print_doc(prefix + "module %s" % m.__name__, m)

    for (name, value) in getmembers(m, isclass):
        if name == '__class__': continue
        print_docstrings(value, prefix=name + ".")

    for (name, value) in getmembers(m, ismethod):
        print_doc("%s%s()" % (prefix, name), value)

    for (name, value) in getmembers(m, isfunction):
        print_doc("%s%s()" % (prefix, name), value)
    

if __name__ == "__main__":
    import sys
    import doctest

    for arg in sys.argv[1:]:
        if arg.startswith("-"): continue
        print "==============================="
        print "== Processing module %s" % arg
        print "==============================="
        m = __import__(arg)
        print_docstrings(m)
        print "Running doctests for %s" % arg
        print "-------------------------------"
        doctest.testmod(m)
