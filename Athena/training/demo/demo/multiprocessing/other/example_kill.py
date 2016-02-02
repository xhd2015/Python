from multiprocessing import Process
import time


def func():
    k = 0
    while True:
        print "func: k =", k
        k += 1
        time.sleep(1)

if __name__ == "__main__":
    print "main: starting func() in a process"
    p = Process(target=func)
    p.start()
    print "main: waiting a bit"
    time.sleep(5)
    print "main: killing the process"
    p.terminate()
    # Wait for it to finish terminating.
    p.join()
    print "main: done"
