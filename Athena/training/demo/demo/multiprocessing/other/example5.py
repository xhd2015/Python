from multiprocessing import Process, Lock


def func(lock, num):
    # Ensure that only one process prints at a time.
    lock.acquire()
    print "%d: Here I am" % num
    print "%d: ---------" % num
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    for num in range(10):
        Process(target=func, args=(lock, num)).start()
