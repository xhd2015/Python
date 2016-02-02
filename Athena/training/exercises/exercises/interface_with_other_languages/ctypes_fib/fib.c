
// Compute the nth Fibonacci number from the sequence that
// begins [0,1,1,2,3,5,...].

int fib(int n)
{
    int result;
    
    if (n < 0)
        result = 0;
    else if (n < 2)
        result = n;
    else
        result = fib(n-1) + fib(n-2);    
    return result;
}        

float _sum(float* val, int length)
{
    float sum = 0.0;
    int i;
    for (i = 0; i < length; i++)
    {
        sum += val[i];
    }
    return sum;
} 

typedef struct 
{
    double x;
    double y;
} coord;
    
double _sum2(coord* val, int length)
{
    double sum = 0.0;
    int i;
    for (i = 0; i < length; i++)
    {
        sum += val[i].x + val[i].y;
    }
    return sum;
} 
