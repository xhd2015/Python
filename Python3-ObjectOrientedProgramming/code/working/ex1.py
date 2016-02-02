__author__ = 'Plamen'

PI = 3.1416


def sum(lst):
    tot = lst[0]
    for value in lst[1:]:
        tot = tot + value
    return tot

w = [0,1,2,3]
print sum(w), PI