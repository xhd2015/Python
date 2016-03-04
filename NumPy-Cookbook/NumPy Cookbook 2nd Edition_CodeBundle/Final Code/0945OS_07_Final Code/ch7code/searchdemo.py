import numpy

def search(n):
   a = numpy.arange(n)
   numpy.searchsorted(a, 42)

sizes = 2 ** numpy.arange(0, 22)

for n in sizes:
   search(n)
