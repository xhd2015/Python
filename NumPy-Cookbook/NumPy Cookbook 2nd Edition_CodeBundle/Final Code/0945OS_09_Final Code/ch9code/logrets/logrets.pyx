from libc.math cimport log
import numpy

def logrets(numbers):
   logs = [log(x) for x in numbers] 
   return numpy.diff(logs)

