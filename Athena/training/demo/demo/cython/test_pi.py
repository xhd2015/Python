import pi
import sys
import time

def f2(r) :
    retList = []
    for i in range(r):
        retList.append(3.14159 * i)
    return retList

def test(r) :
    startTime = time.time()
    pi.f1(r)
    print "CYTHON TOOK: %2.6f for %s" % (time.time()-startTime, r)

    startTime = time.time()
    f2(r)
    print "PURE PYTHON TOOK: %2.6f for %s" % (time.time()-startTime, r)
    
if __name__ == "__main__":
    test(int(sys.argv[1]))
