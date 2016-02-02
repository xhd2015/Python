import multiprocessing as mp

def worker(q):
    v = q.get() # blocking!
    print "got '{}' from parent".format(v)

if __name__ == '__main__':
    q = mp.Queue()
    p = mp.Process(target=worker, args=(q,))
    p.start() # blocks at q.get()
    v = 'parent'
    print "putting '{}' on queue".format(v)
    q.put(v)
    p.join()
