import multiprocessing as mp
from time import sleep

def pingpong(q, name):
    while True:
        v = q.get() # blocking!
        sleep(1.0)
        print "got '{}', sending '{}'".format(v, name)
        q.put(name)

if __name__ == '__main__':

    q = mp.Queue()
    ping = mp.Process(target=pingpong, args=(q, 'ping'))
    pong = mp.Process(target=pingpong, args=(q, 'pong'))
    # have to prime the queue, else deadlock
    q.put('pong')
    ping.start()
    pong.start()
