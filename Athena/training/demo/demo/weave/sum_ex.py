import time

from numpy import array, arange

from scipy import weave

def weave_sum(a):
    """ Build a 'sum' method that will work on contiguous
        1D arrays.
    """    
    code = """
           double sum = 0.0;
           for(int i=0; i < Na[0]; i++)
              sum += a[i];
           return_val = sum;   
           """
    return weave.inline(code,['a'],compiler='gcc')

# compile (if necessary) and print the result.
a = array([1,2,3,4.0])
print "sum:", weave_sum(a)


############################################################################
# Compare the weave_sum to the built in 'sum' function on for a list as well
# as to a numpy array sum method.

for i in range(7):
    size = 10**i
    a = arange(size) # array
    l = range(size)  # list
    print 'size:', size
    t1=time.clock(); b = weave_sum(a); t2=time.clock(); 
    weave_time = (t2-t1)/1e-3    
    t1=time.clock(); b = a.sum(); t2=time.clock(); 
    numpy_time = (t2-t1)/1e-3
    t1=time.clock(); b = sum(l); t2=time.clock(); 
    list_time = (t2-t1)/1e-3
    print 'list, numpy, weave (ms): %4.4f, %4.4f, %4.4f' % \
          (list_time, numpy_time, weave_time)
    print 'numpy/list, numpy/weave: %3.2f, %3.2f' % \
          (numpy_time/list_time, numpy_time/weave_time)