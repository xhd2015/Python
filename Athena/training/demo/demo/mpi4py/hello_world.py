'''
hello_mpi.py -- Trivial mpi4py program to verify correct setup.

To run this program with 4 processes, the commandline invocation is likely
something like:

    $ mpiexec -n 4 python hello_mpi.py
'''

# Importing MPI from mpi4py automatically handles `MPI_Init()` and ensures
# that `MPI_Finalize()` is called when the program ends.
from mpi4py import MPI

# `comm` is the default communicator group with every available process
# participating.
comm = MPI.COMM_WORLD

# The size (number of processes) in COMM_WORLD
size = comm.Get_size()

# `rank` is the index that labels *this* process, guaranteed to be a unique
# integer between 0..size-1 inclusive.

rank = comm.Get_rank()

# The rank 0 process (since it is guaranteed to exist for any mpi program) is
# responsible for communication with the external world, reading in the
# initialization parameters and initializing the remaining processes; the
# remaining processes are typically set up to be primarily workers.

# Give some feedback on which rank we are.  Since we do not do any locking or
# synchronization, the order of output to screen is not defined.

print "Hello, I am {} of {}.".format(rank, size)

# Each process has access to all of Python; here we import a stdlib module and
# sleep a different amount of time before exiting.
from time import sleep
sleep(rank)
