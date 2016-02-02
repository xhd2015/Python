"""Plot the data from demo.h5 (created by tables_demo1.py)."""

import tables as tbl
import matplotlib.pyplot as plt


h5file = tbl.openFile('demo.h5', 'r')

# Use the dotted attribute style to get the arrays from the 'series1' group.
t1 = h5file.root.series1.t
y1 = h5file.root.series1.y

# Use getNode() to get the arrays in the 'series2' group (an alternative to
# the dotted attribute style used above).
t2 = h5file.getNode("/series2", "t")
y2 = h5file.getNode("/series2", "y")

# Note: t1, y1, t2 and y2 are PyTables Array instances.  The actual data for
# each array is on the disk; it has not been read into memory.  These objects
# can be indexed like numpy arrays, and they work with matplotlib for plotting.
# To actually load the data into memory (as true numpy arrays), we could call
# the read() method of the instances.

# Plot the data.  Use the 'TITLE' attribute of the respective hdf5 groups
# as the labels.
plt.plot(t1, y1, label=h5file.root.series1._v_attrs.TITLE)
plt.plot(t2, y2, label=h5file.root.series2._v_attrs.TITLE)
plt.legend(loc='best')
plt.xlabel('time')
plt.show()

h5file.close()
