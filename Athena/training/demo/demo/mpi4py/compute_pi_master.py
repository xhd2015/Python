"""
An mpi4py program that demonstrates spawning worker processes
from a master process.  Run this script as a regular python
program--don't use mpiexec.
"""

from mpi4py import MPI
import numpy
import sys

comm = MPI.COMM_SELF.Spawn(sys.executable, args=['compute_pi_worker.py'], maxprocs=2)

N = numpy.array(1000, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE], op=MPI.SUM, root=MPI.ROOT)
print (PI)
comm.Disconnect()
