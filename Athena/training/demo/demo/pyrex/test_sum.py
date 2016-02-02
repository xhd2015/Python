import time
from numpy import arange

# Use larger array for numpy/pyrex than for python
# because the pytohn version is so slow...
a= arange(1.e6)

print 'elements:', len(a)

t1 = time.time()
res = sum(a)
t2 = time.time()
print 'python sum(approx sec, result):', (t2-t1)*10, res

a= arange(1.e7)
t1 = time.time()
res = a.sum()
t2 = time.time()
print 'numpy sum(sec, result):', t2-t1, res

from sum import sum
t1 = time.time()
res = sum(a)
t2 = time.time()
print 'pyrex sum(sec, result):', t2-t1, res
