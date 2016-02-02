'''
sendrecv.py -- implementation of deadlock.py using sendrecv() to
prevent...deadlock.

`sendrecv()` is guaranteed not to deadlock in situations where pairs of
blocking sends and receives may deadlock.

The semantics of a send-receive operation is what would be obtained if the
caller forked two concurrent threads, one to execute the send, and one to
execute the receive, followed by a join of these two threads.

'''

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# does a circular shift.

arr = np.empty(2, dtype='i')
arr.fill(rank)
dest = rank + 1 % size
source = rank - 1 % size

raise RuntimeError("Finish me!!!")
comm.Sendrecv(sendbuf=arr[-1:], dest=

if rank == 0:
    sendobj = [1, 2, 3]
    lst = comm.sendrecv(sendobj, dest=1, sendtag=0, source=1, recvtag=1)
    print "sent {}, received {}, rank {}".format(sendobj, lst, rank)
elif rank == 1:
    sendobj = [3, 4, 5]
    lst = comm.sendrecv(sendobj, dest=0, sendtag=1, source=0, recvtag=0)
    print "sent {}, received {}, rank {}".format(sendobj, lst, rank)
