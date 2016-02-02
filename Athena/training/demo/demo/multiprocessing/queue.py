import multiprocessing as mp
from time import sleep

def worker(interval, q):
    name = mp.current_process().name
    while True:
        v = q.get() # blocking!
        sleep(interval)
        print "worker '{}', processing value {!r}".format(name, v)
        if v == 'exit':
            break

if __name__ == '__main__':

    q = mp.Queue()
    fast_process = mp.Process(target=worker, args=(1, q,))
    fast_process.name = 'fast worker'
    slow_process = mp.Process(target=worker, args=(2, q,))
    slow_process.name = 'slow worker'

    fast_process.start()
    slow_process.start()

    name = mp.current_process().name

    for x in [1, 3, 5, object(), 'foobar', 'exit', 'exit', 'should never be received']:
        print "{}: putting {!r} on queue".format(name, x)
        q.put(x)
    print
    fast_process.join()
    slow_process.join()
