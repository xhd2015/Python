# This example demonstrates a naive use of threads that change a global variable.
# By using a lock around the code that changes x, we avoid the problem
# demonstrated in demo_problem.py.

import threading

x = 0

def foo(num_iters, xlock):
    """
    This function adds num_iters to the global variable x by adding 1 to
    x num_iters times.
    
    xlock must be a threading.Lock instance.
    """
    global x
    for i in xrange(num_iters):
        xlock.acquire()
        x += 1
        xlock.release()
        # Note: the previous three lines can be replaced with
        # with xlock:
        #     x += 1
        # because the Lock class provides the context manager interface.


if __name__ == "__main__":
    num_iters = 1000000

    # Create the lock that will be used to ensure that changes to x are atomic.
    xlock = threading.Lock()

    # Create two threads, where each target functon is foo()
    t1 = threading.Thread(target=foo, args=(num_iters, xlock))
    t2 = threading.Thread(target=foo, args=(num_iters, xlock))

    # Start the threads.
    t1.start()
    t2.start()

    # Wait for each thread to finish.
    t1.join()
    t2.join()

    print "x =", x
    print "The correct value is %d." % (2*num_iters)
