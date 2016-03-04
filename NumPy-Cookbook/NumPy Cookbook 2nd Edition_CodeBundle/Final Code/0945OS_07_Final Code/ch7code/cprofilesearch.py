import numpy
import cProfile

def search(size):
   random_values = numpy.random.random_integers(-2 * size, 2 * size, size)
   numpy.searchsorted(numpy.arange(size), random_values)

cProfile.run('search(%d)' %(2))
