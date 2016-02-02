import multiprocessing as mp

def worker(p):
    msg = 'whiskey tango fox trot'
    print "sending {!r} to parent".format(msg)
    p.send(msg)
    v = p.recv()
    print "received {!r} from parent".format(v)

if __name__ == '__main__':
    # The two ends of the pipe; each end can send() or recv()
    p_conn, c_conn = mp.Pipe()
    p = mp.Process(target=worker, args=(c_conn,))
    p.start()

    msg = 'foobar'
    print "received {!r} from child".format(p_conn.recv())
    print "sending {!r} to child".format(msg)
    p_conn.send(msg)
    p.join()
