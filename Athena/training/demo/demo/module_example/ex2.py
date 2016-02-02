" An example module "

PI = 3.1416


def sum(lst):
    """ Sum the values in a list.
    """
    tot = 0
    for value in lst:
        tot = tot + value
    return tot


def add(x, y):
    " Add two values."
    a = x + y
    return a


def test():
    w = [0, 1, 2, 3]
    assert (sum(w) == 6)
    print 'test passed'


print __name__

# This code runs only if this
# module is the main program.
if __name__ == '__main__':
    test()
