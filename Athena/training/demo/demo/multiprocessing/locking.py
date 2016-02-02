import multiprocessing as mp


class PrintLock(object):
    def __init__(self, lk):
        self.lk = lk

    def prnt(self, s):
        name = mp.current_process().name
        with self.lk:
            for i in range(100):
                print s, "from process", name


def print_lock(lk, i):
    name = mp.current_process().name
    lk.acquire()
    for j in range(100):
        print i, "from process", name
    lk.release()


if __name__ == '__main__':
    lk = mp.Lock()
    ps = [mp.Process(target=print_lock, args=(lk, i)) for i in range(100)]
    [p.start() for p in ps]
    [p.join() for p in ps]

    # This is an object-oriented version...
    obj_p = [mp.Process(target=PrintLock(lk).prnt, args=(i,)) for i in range(100)]
    [p.start() for p in obj_p]
    [p.join() for p in obj_p]
