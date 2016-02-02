#include <math.h>
#include "fancy_science.h"

#define speed_of_light 299792458.0
#define sq(x) ((x) * (x))

double my_hypot(double a, double b)
{
    return sqrt(a*a + b*b);
}

double eulers_number(int n)
{
    double e = 1.0; /* n==0 case */
    
    e = pow(1.0 + 1.0/n, n);
    
    return e;
}

float energy(float mass)
{
    return mass * sq(speed_of_light);
}
