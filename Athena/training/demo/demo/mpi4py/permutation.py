
from mpi4py import MPI
import numpy as np

def main(global_n):

    comm = MPI.COMM_WORLD

    rank = comm.Get_rank()
    size = comm.Get_size()

    local_n = global_n / size
    if global_n != local_n * size:
        raise ValueError("global_n != local_n * size")

    if rank == 0:
        glb_perm = np.arange(global_n)
        np.random.shuffle(glb_perm)
        rhs = np.arange(global_n)
        lhs_ans = rhs[glb_perm] # this is the answer.
        glb_lhs = np.empty(global_n, dtype=np.int32)
    else:
        glb_perm = np.array([])
        rhs = np.array([])
        glb_lhs = np.array([])

    # Distribute the rhs and permutations
    local_rhs = np.empty(local_n, dtype=np.int32)
    comm.Scatter(sendbuf=rhs, recvbuf=local_rhs, root=0)

    local_perm = np.empty(local_n, dtype=np.int32)
    comm.Scatter(sendbuf=glb_perm, recvbuf=local_perm, root=0)

    # create the local_lhs
    local_lhs = np.empty(local_n, dtype=np.int32)

    # create the window
    win = MPI.Win.Create(local_rhs, comm=comm)

    local_buf = np.zeros_like(local_lhs)

    if 1: # debugging win.Get(...) issues
        win.Fence()
        target_rank = int(not rank)
        win.Get(local_buf, target_rank, target=3)
        win.Fence()

        res = "{} {} {}".format(rank, target_rank, local_buf)

        pp = comm.gather(res, root=0)

        if rank == 0:
            for x in pp:
                print x

    if 0: # original code
        # This is horribly slow (for loop in python over expensive communication)
        # This would be an ideal operation to speed up with Cython.
        win.Fence()
        for idx, p in enumerate(local_perm):
            target_rank = p / local_n
            win.Get(local_buf, target_rank)
            if rank == 0:
                print target_rank, local_buf
            target_idx = p % local_n
            local_lhs[idx] = local_buf[target_idx]
        win.Fence()
    win.Free()

    comm.Gather(sendbuf=local_lhs, recvbuf=glb_lhs, root=0)

    if rank == 0:
        print np.allclose(glb_lhs, lhs_ans)
        print len(lhs_ans), lhs_ans
        print len(glb_lhs), glb_lhs


if __name__ == '__main__':
    main(16)
