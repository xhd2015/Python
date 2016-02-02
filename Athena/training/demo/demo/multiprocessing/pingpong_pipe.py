import multiprocessing as mp
from time import sleep

def pingpong(c, name):
    c.send(name) # ensure no deadlock.
    while True:
        v = c.recv() # blocking!
        sleep(1.0)
        print "got '{}', sending '{}'".format(v, name)
        c.send(name)

if __name__ == '__main__':
    a, b = mp.Pipe()
    ping = mp.Process(target=pingpong, args=(a, 'ping'))
    pong = mp.Process(target=pingpong, args=(b, 'pong'))
    ping.start()
    pong.start()
