from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
vers = MPI.Get_version()

a = np.arange(size, dtype='i') + rank * 100
b = np.zeros(size, dtype='i')
a.fill(rank)

comm.Barrier()

print "process {} has the following: {}".format(rank, a)
win = MPI.Win.Create(a, comm=comm)

win.Fence(MPI.MODE_NOPUT | MPI.MODE_NOPRECEDE)
for i in range(size):
    win.Get(b[i:i+1], i, target=i)
win.Fence(MPI.MODE_NOSUCCEED)

print "process {} obtained the following: {}".format(rank, b)
win.Free()
