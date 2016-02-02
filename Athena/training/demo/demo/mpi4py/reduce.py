
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

arr = np.arange(rank * 3, (rank + 1) * 3)

if rank == 0:
    recvbuf = np.zeros(3, dtype='i')
else:
    recvbuf = None

comm.Reduce(sendbuf=arr, recvbuf=recvbuf, root=0)

if rank == 0:
    print recvbuf
