#include <hypot.h>
#include <stdio.h>

int main()
{
    float a, b, c;
    
    a = 3.0;
    b = 4.0;
    
    c = my_hypot(a,b);
    
    printf("The hypotenuse of a triangle with sides %3.1f and %3.1f is %3.1f.\n", a,b,c);
    
    return 0;
}
