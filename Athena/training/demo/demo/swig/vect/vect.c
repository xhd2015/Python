
#include <stdlib.h>
#include "vect.h"

int *vect(int x, int y, int z)
{
    int *res;

    res = (int *) malloc(3 * sizeof(int));
    res[0] = x;
    res[1] = y;
    res[2] = z;
    return res;
}

int sum(int *v)
{
    return v[0] + v[1] + v[2];
}
