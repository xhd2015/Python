from multiprocessing import Process, Queue


def func(q):
    q.put(dict(value=100, name='foo'))


if __name__ == "__main__":
    q = Queue()
    proc = Process(target=func, args=(q,))
    proc.start()
    print q.get()
    proc.join()
