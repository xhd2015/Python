# This example demonstrates a naive use of threads that change a global variable.
# Because changes to the global variables are not made atomically, the final
# result is incorrect.

import threading

x = 0

def foo(num_iters):
    """
    This function adds num_iters to the global variable x by adding 1 to
    x num_iters times.
    """
    global x
    for i in xrange(num_iters):
        x += 1


if __name__ == "__main__":
    num_iters = 1000000

    # Create two threads, where each target functon is foo()
    t1 = threading.Thread(target=foo, args=(num_iters,))
    t2 = threading.Thread(target=foo, args=(num_iters,))

    # Start the threads.
    t1.start()
    t2.start()

    # Wait for each thread to finish.
    t1.join()
    t2.join()

    print "x =", x
    print "The correct value is %d." % (2*num_iters)
