"""
Documentation is available here: 

    * http://netcdf4-python.googlecode.com/svn/trunk/docs/netCDF4-module.html
    * http://code.google.com/p/netcdf4-python/
"""
from numpy.random import random
import netCDF4
import os
from pylab import plot, show, title
import time
import warnings


def write_nc(filename):
    """ Example illustrating how to write a new netCDF file
    """
    # Cannot open an existing file in write mode.
    if os.path.exists(filename):
        warn_msg = "%s already exists: erasing it..." % filename
        warnings.warn(warn_msg)
        os.remove(filename)

    # Create a new dataset: it create a "root group" analogous to the root directory
    # of a UNIX filesystem
    rootgrp = netCDF4.Dataset(filename, mode='w')

    # Create a new group: think of it as a folder in the dataset
    timeseries_group = rootgrp.createGroup('forecast')
    timeseries_group = rootgrp.createGroup('timeseries')

    # Create a couple of new dimensions. The first one has no predefined size.
    # This allow to append an (almost) infinite amount of data in this dimension
    rootgrp.createDimension('daily_sec_ts', size=None)
    rootgrp.createDimension('time', size=10)

    # Create the variable that will contain the data. The dimensions must already
    # exist in the group the variable is in
    storage = timeseries_group.createVariable('ts1', 'f8', dimensions=('time', 'daily_sec_ts'))

    # add experiment results to the storage
    for i in range(10):
        # use slicing to add the data
        storage[i, :3600] = random((3600,))

    # Add some metadata on the fly
    rootgrp.description = "This is a new test file"
    rootgrp.history = "File created on %s" % time.ctime(time.time())

    # By default, the netCDF format uses mmap, so make sure all data is written to disk with
    rootgrp.sync()

    # add some plotting based on that (looping on a group)

    # Close the file
    rootgrp.close()


def read_nc(filename):
    """ Example illustrating how to read a file 
    """
    print "Opening netCDF file %s" % filename
    new_rootgrp = netCDF4.Dataset(filename, mode='r')
    print "File format:", new_rootgrp.file_format
    print "Metadata :"
    for attr in new_rootgrp.ncattrs():
        print " " * 4, attr, ":", getattr(new_rootgrp, attr)

    print "Structure of the content:", new_rootgrp.groups.keys()
    print "Dimensions defined at the top level:"
    for dim, val in new_rootgrp.dimensions.items():
        print "    Dimension %s of length %s" % (dim, len(val))
    for child_grp in new_rootgrp.groups.values():
        if child_grp.groups:
            print " " * 8 + "Content of %s is " % (child_grp, child_grp.groups)
        if child_grp.dimensions:
            for dim, val in new_rootgrp.dimensions.items():
                print " " * 8 + "Dimension %s for length %s" % (dim, len(val))

    ts1 = new_rootgrp.groups["timeseries"].variables["ts1"]
    # This is to illustrate the differences in behaviors between slicing a netCDF variable
    # and a numpy array. The result of the fancy indexing below would have been of shape (3,)
    # in Numpy
    print ("Note: Fancy indexing in netCDF behaves differently from Numpy:\nts1[[1,2,3],"
           "[1,2,3]]=\n%s" % ts1[[1, 2, 3], [1, 2, 3]])

    plot(ts1[0, :100])
    title("Slice of data from %s" % filename)
    show()
    return


if __name__ == "__main__":
    filename = 'timeseries_data.nc'
    write_nc(filename)
    read_nc(filename)
