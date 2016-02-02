from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if not rank:
    a_send = np.arange(100).reshape(10, 10)
    print a_send
    comm.Send([a_send, MPI.INT], dest=1, tag=13)
elif rank == 1:
    a_recv = np.empty(100, dtype='i').reshape(10, 10)
    comm.Recv([a_recv, MPI.INT], source=0, tag=13)
    print a_recv
    assert np.all(a_recv == np.arange(100).reshape(10, 10))
