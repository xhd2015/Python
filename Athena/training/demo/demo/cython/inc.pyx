# Standard function callable from Python.
def inc(int num, int offset):
   return num + offset 

def inc_seq(seq, offset):
   result = []
   for val in seq:
       res = inc(val, offset)
       result.append(res)
   return result        

# cdef function callable are faster, but only
# callable in Cython file.
cdef int inc_fast(int num, int offset):
   return num + offset 

def fast_inc_seq(seq, offset):
   result = []
   for val in seq:
       res = inc_fast(val, offset) 
       result.append(res)
   return result        
