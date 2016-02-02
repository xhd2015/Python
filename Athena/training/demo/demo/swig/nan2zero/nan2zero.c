
#include <math.h>

/*
 *  In the double array of length len, replace any occurrence
 *  of NaN by zero.
 */
void nan_to_zero_double(int len, double *array)
    {
    int i;

    for (i = 0; i < len; ++i, ++array)
        {
        if (isnan(*array))
            *array = 0.0;
        }
    }


/*
 *  In the float array of length len, replace any occurrence
 *  of NaN by zero.
 */

void nan_to_zero_float(int len, float *array)
    {
    int i;

    for (i = 0; i < len; ++i, ++array)
        {
        if (isnan(*array))
            *array = 0.0;
        }
    }
