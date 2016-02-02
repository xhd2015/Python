
#include <stdio.h>

double myfunc(double *x);

int main(int argc, char *argv[])
{
	double x = 5.0;

	printf("myfunc(%g) = %g\n", x, myfunc(&x));
	return 0;
}
