"""mpi4py demo: point-to-point communication of a python object."""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = dict(a=7, b=3.14)
    comm.send(data, dest=1, tag=11)
    print "Sent", data
else:
    data = comm.recv(source=0, tag=11)
    print "Received", data