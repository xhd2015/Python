#include <math.h>
#include "rms.h"

double rms(double *seq, int n)
{
    int k;
    double sum;

    sum = 0.0;
    for (k = 0; k < n; ++k) {
        sum += seq[k] * seq[k];
    }
    return sqrt(sum / n);
}
