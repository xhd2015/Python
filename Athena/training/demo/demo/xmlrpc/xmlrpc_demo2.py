"""XML-RPC demo.

This demo is a variation of xmlrpc_demo.py.  Instead of using a
custom handler with its _dispatch() method overridden, we use the
server's register_function() method to declare the functions that
are exposed by the server.

Two functions are provided: fact(n) and fib(n).
"""

#----------------------------------------------------------------------------
# Define the functions provided by the server.
#----------------------------------------------------------------------------

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


def fib(n):
    f = 1
    f0, f1 = 0, 1
    for k in xrange(n):
        f = f0 + f1
        f0, f1 = f1, f
    return f

#----------------------------------------------------------------------------
# Functions to start a server or to run a test client.
#----------------------------------------------------------------------------

from SimpleXMLRPCServer import SimpleXMLRPCServer


def run_server(port):
    server = SimpleXMLRPCServer(("localhost", port))
    # Register the functions provided by the server.
    server.register_function(fact)
    server.register_function(fib)
    print 'Server running on port: %d' % port
    server.serve_forever()


def test_client():
    import xmlrpclib
    svr = xmlrpclib.Server("http://localhost:8001")
    print 'factorial of 10 from "http://localhost:8001":', svr.fact(10)
    print '5th term of Fibonacci seq from "http://localhost:8001":', svr.fib(5)


if __name__ == "__main__":
    port = 8001
    run_server(port)
