'''
deadlock.py -- illustrates an mpi program that will deadlock.

from: www.mpi-forum.org/docs, adapted to mpi4py.

The receive operation of the first process must complete before its send, and
can complete only if the matching send of the second processor is executed. The
receive operation of the second process must complete before its send and can
complete only if the matching send of the first process is executed. This
program will always deadlock. The same holds for any other send mode.

'''

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    arr = np.empty(100, dtype='i')
    req = comm.Irecv(arr, source=1, tag=1)
    req.Wait()
    comm.send(arr+1, dest=1, tag=1)
elif rank == 1:
    arr = np.arange(10)
    lst = comm.recv(source=0, tag=1)
    comm.send([3,4,5], dest=0, tag=1)
