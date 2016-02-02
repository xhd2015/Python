#include <iostream>
#include "fancy_science.h"

int main(int argc, char **argv)
{
    const int n = 1000000;

    std::cout << "eulers_number(" << n << "): " << eulers_number(n) << std::endl;

    return 0;
}
