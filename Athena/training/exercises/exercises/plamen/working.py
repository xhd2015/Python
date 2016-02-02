PI = 3.14159


def sum1(lst):
    tot = 0
    for value in lst:
        tot = tot + value
    return tot


w = [0, 1, 2, 3, 4]
print sum1(w), PI
