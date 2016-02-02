import time
from numpy import arange, float32, logspace, linspace
from scipy import weave

code = """
       #define ALIGNMENT 16
       #define ELEMENTS_PER_VECTOR 4
       #define BYTES_PER_ELEMENT 4
       #define min(x,y) (x)<(y)?(x):(y)
       
       /* Use SSE to calc sum(a) */
       
       // Create the accumulator vector and initialize to zero.
       __m128 vec_accum = _mm_set_ps(0.0, 0.0, 0.0, 0.0);       
       float* fp_accum = (float*)&vec_accum;
       __m128 vec_a;
       
       // Find how many bytes the array is mis-aligned.
       int byte_alignment_offset = ((int) a) % ALIGNMENT;       
       // The initial elements in the numpy array are not on a byte boundary.
       int leading_count = byte_alignment_offset/BYTES_PER_ELEMENT;
       // The number of SSE vectors in the "middle" of the array.
       int vector_count;
       // The end of the array that is is less than the size of a vector op.
       int trailing_count;
       
       if (Na[0] > leading_count)
       {
           vector_count = (Na[0] - leading_count) / ELEMENTS_PER_VECTOR;
           trailing_count = (Na[0] - leading_count) % ELEMENTS_PER_VECTOR;
       }
       else
       {
           leading_count = min(Na[0], leading_count);
           vector_count = 0;
           trailing_count = 0;
       }

       // Create a copy of the pointer for use in vector algorithm.
       float* a_ptr = a + leading_count;
       int i;
       float sum = 0.0;
       int items = 0;
       
       /* load any leading values from that are missed because of aligment. */
       for (i=0;i<leading_count;i++)
       {
           // fp_accum is the same as vec_accum, so we're loading it up 
           // with the "leading" values from the a array.
           fp_accum[i] = a[i];
           //items++;
       }       

       for(i=0;i<vector_count;i++) 
       {        
           // load a segment of the a array
           vec_a = _mm_load_ps(a_ptr);
           // vec_accum += vec_a
           vec_accum = _mm_add_ps(vec_a, vec_accum);
           // address next segment
           a_ptr += ELEMENTS_PER_VECTOR;
           //items += ELEMENTS_PER_VECTOR;
       }
       
       // and cleanup anything that is left over from original array
       for (i=0;i<trailing_count;i++)
       {
           sum += a_ptr[i];
           //items++;
       }
       // add the accumulated values to get their total sum 
       // fp_accum points to memory in vec_accum.
       for (i=0;i<ELEMENTS_PER_VECTOR;i++)
       {
           sum  += fp_accum[i];
       }                      

       py::dict result; 
       result["sum"] = sum;
       result["items"] = items;
       result["leading_count"] = leading_count;
       result["trailing_count"] = trailing_count;
       result["vector_count"] = vector_count;
       return_val = result;
       //return_val = sum;       
       """

for size in arange(1,10000):
#for size in logspace(1,6, 10):
    #a = (arange(int(size),dtype=float32)+1)*2
    a = logspace(1,2,int(size)).astype(float32)
    #a = a[::-1].copy()
        
    t1 = time.clock()
    result = weave.inline(code, ['a'], compiler='gcc',
                          verbose=2,
                          headers = ['<xmmintrin.h>'],
                          extra_compile_args=['-msse'],
                          extra_link_args=['-msse'])
    t2 = time.clock()                 
    vec_time = t2-t1

    t1 = time.clock()
    numpy_result = a.sum()
    t2 = time.clock()                 
    numpy_time = t2-t1
    
    print 'size: %3.2f' % size
    print 'value:', numpy_result, result["sum"]
    print 'items:', len(a), result["items"]
    print 'error: %f' % (numpy_result - result["sum"])
    #print 'value:', numpy_result, result
    print 'items:', len(a), result["items"]
    #print 'error: %f' % (numpy_result - result)
    print 'numpy: %3.2f' % (numpy_time*1e6)
    print 'vector: %3.2f' % (vec_time*1e6)
    print 'speed_up: %3.2f' % (numpy_time/vec_time)
    print result['leading_count'], result['vector_count'], result['trailing_count']
    print
    if (numpy_result - result["sum"]) > .000001:
        print 'oops'
        from numpy import diff
        aa = a.copy()
        #print aa
        for i in range(len(aa)):
            a = aa[:i+1]
            result = weave.inline(code, ['a'], compiler='gcc',
                      verbose=2,
                      headers = ['<xmmintrin.h>'],
                      extra_compile_args=['-msse'],
                      extra_link_args=['-msse'])
    
            print a.sum(), result["sum"], a.sum()-result["sum"]
        
        break