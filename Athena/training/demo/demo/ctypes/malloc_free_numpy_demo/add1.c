
#include <stdlib.h>

/*
 *  add1: Add 1.0 to each element in the array vec.
 */

float *add1(float *vec, int len)
{
    float *ret;
    int i;
    
    ret = (float *) malloc(len*sizeof(float));
    for (i = 0; i < len; i++)
        ret[i] = vec[i] + 1.0;
    return ret;
}
