
def receiving_generator():
    while True:
        val = (yield)
        print "Received", val

def transmitting_receiving_generator():
    i = -1
    while True:
        i += 1
        val = (yield i)
        print "Received", val

