"""
Example of using the with statement to make a temporary tweak to
global settings.

Here we create a class that lets us use extended precision when
working with Decimal instances.

The block following the with statement might be left

  (a) normally, after executing all the statements in the block, or
  (b) as the result of an exception, or
  (c) as the result of a return within the block.

No matter how the with block is left, the __exit__ method of the
context manager will be called.

"""

# Necessary for Python 2.5; don't need this in Python >= 2.6.
from __future__ import with_statement

from decimal import Decimal, getcontext


class precision(object):
    """
    Context manager for temporarily changing the precision
    of a Decimal calculation.

    """

    def __init__(self, new_precision):
        self.new_precision = new_precision

    def __enter__(self):
        """Setup: Store the old precision, and change the current precision. """
        context = getcontext()
        self.old_precision = context.prec
        context.prec = self.new_precision

    def __exit__(self, *exception_info):
        """Cleanup: restore the old precision. """
        context = getcontext()
        context.prec = self.old_precision


# Managing precision without 'with':
old_precision = getcontext().prec
getcontext().prec = 200
# Do high-precision computations here
# Reset the precision
getcontext().prec = old_precision

# Managing precision using 'with'
with precision(200):
    print "Current precision is: ", getcontext().prec
    x = Decimal(2).sqrt()
    print "sqrt(2) = ", x

print "Left with statement.  Precision is now: ", getcontext().prec
