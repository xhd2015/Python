from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if not rank:
    d_send = {'a':{1:2}, 'b':[1,2,3]}
    comm.send(obj=d_send, dest=1, tag=13)
elif rank == 1:
    d_recv = comm.recv(source=0, tag=13)
    assert d_recv == {'a':{1:2}, 'b':[1,2,3]}
