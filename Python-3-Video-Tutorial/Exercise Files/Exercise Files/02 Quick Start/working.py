__author__ = 'Plamen'

import os
from multiprocessing import Process


def func(value):
    info('func')
    print("value =", value)


def info(name):
    """Print my process id and the process id of my parent."""
    print("%s:  pid=%s  parent=%s" % (name, os.getpid(), os.getppid()))


if __name__ == "__main__":
    info('main')

    # Create the Process object that will run func(10).
    proc = Process(target=func, args=(10,))

    # Spawn and execute the process.
    proc.start()

    # Wait for proc to complete.
    proc.join()
