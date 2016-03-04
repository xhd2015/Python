import numpy

def pos_confidence(numbers):
   diffs = numpy.diff(numbers)
   n = float(len(diffs))
   p = len(diffs[diffs > 0])/n
   confidence = numpy.sqrt(p * (1 - p)/ n)

   return (p, confidence)
   
