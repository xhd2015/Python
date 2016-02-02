""" 
Compare the speed of NumPy, weave.blitz and weave.inline for the following
equation::
    
        result=a+b*(c-d)
    
Set up all arrays so that they are one-dimensional and have 1 million 
elements in them.
"""
import time

from numpy import arange, empty, float64
from scipy import weave

N = 1000000

a = arange(N,dtype=float64)
b = arange(N,dtype=float64)
c = arange(N,dtype=float64)
d = arange(N,dtype=float64)

result = empty(N,dtype=float64)

t1= time.clock()
result = a + b*(c-d)
t2=time.clock()
numpy_time = t2-t1

t1= time.clock()
weave.blitz("result = a+b*(c-d)")
t2=time.clock()
blitz_time = t2-t1
print "array size, numpy (sec), blitz (sec), numpy/blitz: %d, %3.2f, %3.2f, %3.2f" % \
      (N, numpy_time, blitz_time, numpy_time/blitz_time)


code = """
       for(int i=0;i<Na[0];i++)
       {
           result[i] = a[i]+b[i]*(c[i]-d[i]);
       }
       """


t1= time.clock()
weave.inline(code,['a','b','c','d','result'], compiler='gcc')
t2=time.clock()
inline_time = t2-t1
print "array size, numpy (sec), blitz (sec), inline (sec): %d, %3.2f, %3.2f %3.2f" % \
      (N, numpy_time, blitz_time, inline_time)

print 'Speedup for blitz and inline: %3.2f %3.2f' % \
      (numpy_time/blitz_time, numpy_time/inline_time)


    
    