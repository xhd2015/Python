import multiprocessing as mp
from time import sleep
from random import random


def worker(num):
    sleep(2.0 * random())
    name = mp.current_process().name
    print "worker {}, name: {}".format(num, name)


if __name__ == '__main__':

    print "Master name: {}".format(mp.current_process().name)

    for i in range(2):
        p = mp.Process(target=worker, args=(i,))
        p.start()
