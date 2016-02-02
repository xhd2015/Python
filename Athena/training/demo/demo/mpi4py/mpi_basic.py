'''
mpi_basic.py -- Sanity check that MPI4Py is working.

Run from the commandline with the equivalent of 

    $ mpiexec -n 4 python mpi_basic.py

Will result in "Hello, world!" output 4 times, and verifies that your system
has been properly set up.

'''

from mpi4py import MPI
import os

print "Hello, world!", os.getpid()
