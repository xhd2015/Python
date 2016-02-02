'''
requires_buffer.py -- illustrates an mpi program that will deadlock.

from: www.mpi-forum.org/docs, adapted to mpi4py.

The message sent by each process has to be copied out before the send
operation returns and the receive operation starts. For the program to
complete, it is necessary that at least one of the two messages sent be
buffered. Thus, this program can succeed only if the communication system
can buffer at least count words of data.

'''

from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0:
    comm.send([1,2,3], dest=1, tag=1)
    lst = comm.recv(source=1, tag=1)
elif rank == 1:
    comm.send([3,4,5], dest=0, tag=1)
    lst = comm.recv(source=0, tag=1)

