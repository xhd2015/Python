from mpi4py import MPI
from cPickle import dumps

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

class Params(object):
    ''' All processes have access to the Params class definition.
    '''
    def __init__(self, temp):
        self.temp = temp

if not rank:
    p0 = Params(temp=12.0)
    comm.send(p0, dest=1, tag=17)
if rank == 1:
    p1 = comm.recv(source=0, tag=17)
    print dumps(p1)
