'''
If the array is large enough, the following code will deadlock.
'''
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# On my implementation, NN >= 16400 deadlocks, NN < 16300 does not deadlock.
# This is the limit of MPICH-2's internal buffering.
NN = 16400

arr = np.zeros(NN, dtype='i')
arr.fill(rank)

dest = (rank + 1) % size
source = (rank - 1 + size) % size

print "Node {} is sending.".format(rank)
comm.Send(arr, dest=dest)
print "Node {} sent {}..{} successfully.".format(rank, arr[0], arr[-1])

comm.Recv(arr, source=source)
print "Node {} received {}..{} successfully.".format(rank, arr[0], arr[-1])
