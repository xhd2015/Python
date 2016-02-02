
#include <stdio.h>
#include <math.h>

double c_simpson(double (*f)(double *), double *a, double *b, int *n);

double myfunc(double *x)
{
    double y;

    y = cos(*x);
    return y;
}


int main(int argc, char *argv[])
{
    double integral;
    double a, b;
    int n;

    a = 0.0;
    b = 2.0;
    n = 100;

    integral = c_simpson(myfunc, &a, &b, &n);
    printf("simpson: %g\n", integral);
    printf("exact:   %g\n", sin(b) - sin(a));
    return 0;
}
