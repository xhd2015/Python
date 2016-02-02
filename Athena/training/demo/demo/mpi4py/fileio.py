from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

local_n = 128
global_n = size * local_n

nints = global_n / size

arr = np.arange(local_n, dtype=np.int32)

offset = arr.nbytes * rank

fh = MPI.File.Open(comm, 'mpi_trial_file.out', amode=MPI.MODE_WRONLY | MPI.MODE_CREATE)
fh.Write_at(offset, arr)
fh.Close()
