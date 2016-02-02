
import math
from pysimpson import simpson


a = 0.0
b = 2.0
n = 100

intgrl = simpson(math.cos, a, b, n)

print "integrate cos"
print "simpson: ", intgrl
print "exact:   ", math.sin(b) - math.sin(a)
print
