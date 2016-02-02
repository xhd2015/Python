"""mpi4py demo: point-to-point communication with numpy array."""

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Pass explicit MPI data types.
data = numpy.empty(1000, dtype=int)
if rank == 0:
    data = numpy.arange(1000, dtype=int)
    comm.Send([data, MPI.INT], dest=1, tag=77)
    print "Sent array"
elif rank == 1:
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print "Received data"

# Automatic MPI datatype discovery.
data = numpy.empty(1000, dtype=numpy.float64)
if rank == 0:
    data = numpy.arange(1000, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
    print "Sent array"
elif rank == 1:
    comm.Recv(data, source=0, tag=13)
    print "Received data"
