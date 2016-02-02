# Compile this file with 'pycc pi.py'

from numba import export


def multiply_by_pi(num):
    """ Multiply a number by pi. """
    return num * 3.14159265359


export('mult f8(i4)')(multiply_by_pi)
export('mult_f f8(f8)')(multiply_by_pi)
