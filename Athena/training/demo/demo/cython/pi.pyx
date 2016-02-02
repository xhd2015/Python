def multiply_by_pi( int num ) :
   return num * 3.14159265359

def f1( int r ) :
   retList = []
   cdef unsigned int i
   for i in range(r):
      retList.append( 3.14159 * i )
   return retList
   
cdef class Shrubbery: 
   cdef int width, height 
   def __init__(self, w, h): 
      self.width = w 
      self.height = h 
   def describe(self): 
      print "This shrubbery is", self.width, "by", self.height, "cubits."
