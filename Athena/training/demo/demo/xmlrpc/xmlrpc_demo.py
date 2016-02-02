#----------------------------------------------------------------------------
# Define your functions
#----------------------------------------------------------------------------

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

#----------------------------------------------------------------------------
# Code needed from remote calls via xml-rpc
#----------------------------------------------------------------------------

from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from SimpleXMLRPCServer import SimpleXMLRPCServer


class my_handler(SimpleXMLRPCRequestHandler):
    def _dispatch(self, method, params):
        print "CALL", method, params, '-->',
        result = apply(eval(method), params)
        print result
        return result


def run_server(port):
    server = SimpleXMLRPCServer(("localhost", port), my_handler)
    print 'Server running on port: %d' % port
    server.serve_forever()


def test_client():
    import xmlrpclib
    svr = xmlrpclib.Server("http://localhost:8001")
    print 'factorial of 10 from "http://localhost:8001":', svr.fact(10)


if __name__ == "__main__":
    port = 8001
    run_server(port)
