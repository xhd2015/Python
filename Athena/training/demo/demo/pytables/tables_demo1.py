"""Save some numpy arrays to an HDF5 file using PyTables."""

import time
import numpy as np
import tables as tbl


t1 = np.linspace(0, 2*np.pi, 25)
y1 = np.sin(t1)
t2 = np.linspace(0, 2*np.pi, 32)
y2 = np.cos(t2)

# We'll save the arrays organized in two groups, series1 and series2, so the
# layout of the data in the file will be
# /series1/t   (the t1 array)
# /series1/y   (the y1 array)
# /series2/t   (the t2 array)
# /series2/y   (the y2 array)

# Create the pytables file.
h5file = tbl.openFile("demo.h5", mode='w', title='Demonstration')

# Add the 'series1' group.  Use the pythonic naming scheme (h5file.root) to
# indicate where.
h5file.createGroup(h5file.root, "series1", "Time Series 1")

# Add the arrays 't' and 'y' to the 'series1' group.
h5file.createArray(h5file.root.series1, 't', t1, 'Time')
h5file.createArray(h5file.root.series1, 'y', y1, 'Y Values')

# Add the 'series2' group.  Use a string path ("/") to indicate where (compare
# to the creation of "series1" above).
h5file.createGroup("/", "series2", "Time Series 2")

# Add the arrays 't' and 'y2' (as 'y') to the 'series2' group.
h5file.createArray("/series2", 't', t2, 'Time')
h5file.createArray("/series2", 'y', y2, 'Y Values')

# Add a 'timestamp' attribute to all the arrays (demonstrates the use
# of node attributes).
timestamp = time.ctime()
h5file.root.series1.t.attrs.timestamp = timestamp
h5file.root.series1.y.attrs.timestamp = timestamp
h5file.root.series2.t.attrs.timestamp = timestamp
h5file.root.series2.y.attrs.timestamp = timestamp

print
print h5file
print

h5file.close()
