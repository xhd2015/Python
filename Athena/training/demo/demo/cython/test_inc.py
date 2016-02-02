import time
import inc

print inc.inc(3,3)

a = range(100000)

import time
t1 = time.time()
b = inc.inc_seq(a,3)
t2 = time.time()
normal = t2-t1
print 'normal:', normal

t1 = time.time()
b = inc.fast_inc_seq(a,3)
t2 = time.time()
fast = t2-t1
print 'fast:', fast
print 'speedup:', normal/fast

