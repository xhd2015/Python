"""
This script demonstrates the use of a numpy.loadtxt converter and
the function datetime.datetime.strptime to read a column containing
a timestamp in a text file.

The data files are in the "data/" subdirectory.   All the files
except "milliseconds.py" contain the same data, but the timestamp
formats are different.  The timestamps in "milliseconds.py" have
the same date and time, but the 'seconds' field contains a
fractional component.

The following table show a sample timestamp and corresponding
strptime format string for each file:

File               Timestamp                  Format string
---------------    ------------------------   ----------------------
dashes.csv         "2009-08-21 14:10:00"      "%Y-%m-%d %H:%M:%S"
dashes_12hr.csv    "2009-08-21 02:10:00 PM"   "%Y-%m-%d %I:%M:%S %p"
slashes_us.csv     "8/21/2009 14:10:00"       "%m/%d/%Y %H:%M:%S"
slashes_nonus.csv  "21/8/2009 14:10:00"       "%d/%m/%Y %H:%M:%S"
dayofyear.csv      "2009233+141000"           "%Y%j+%H%M%S"
milliseconds.csv   "2009-08-21 14:10:00.375"  "%Y-%m-%d %H:%M:%S.%f"
"""

from datetime import datetime
import numpy as np
from numpy.testing import assert_array_equal


def print_array(a):
    """ Print the structured array `a`. """
    for name in a.dtype.names:
        print "{:27s}".format(name),
    print
    for row in a:
        for name in a.dtype.names:
            print "{:27s}".format(str(row[name])),
        print


# Data type for the structured array to be created by loadtxt.
dt = np.dtype([('time', np.datetime64), ('value', np.float32), ('number', np.int32)])

fmt = "%Y-%m-%d %H:%M:%S"
data = np.loadtxt('data/dashes.csv', delimiter=',', dtype=dt,
                    converters={0: lambda s: datetime.strptime(s, fmt)})
print_array(data)

fmt = "%Y-%m-%d %I:%M:%S %p"
data2 = np.loadtxt('data/dashes_12hr.csv', delimiter=',', dtype=dt,
                    converters={0: lambda s: datetime.strptime(s, fmt)})
assert_array_equal(data, data2)

fmt = "%m/%d/%Y %H:%M:%S"
data2 = np.loadtxt('data/slashes_us.csv', delimiter=',', dtype=dt,
                    converters={0: lambda s: datetime.strptime(s, fmt)})
assert_array_equal(data, data2)

fmt = "%d/%m/%Y %H:%M:%S"
data2 = np.loadtxt('data/slashes_nonus.csv', delimiter=',', dtype=dt,
                    converters={0: lambda s: datetime.strptime(s, fmt)})

assert_array_equal(data, data2)

fmt = "%Y%j+%H%M%S"
data2 = np.loadtxt('data/dayofyear.csv', delimiter=',', dtype=dt,
                    converters={0: lambda s: datetime.strptime(s, fmt)})
assert_array_equal(data, data2)

print
fmt = "%Y-%m-%d %H:%M:%S.%f"
data3 = np.loadtxt('data/milliseconds.csv', delimiter=',', dtype=dt,
                    converters={0: lambda s: datetime.strptime(s, fmt)})
print_array(data3)
