import numpy

def pos_confidence(numbers):
   diffs = numpy.diff(numbers)
   n = len(diffs)
   p = diffs[diffs > 0]/n
   confidence = numpy.sqrt(p * (1 - p) * n)

   return (p, confidence)
   
