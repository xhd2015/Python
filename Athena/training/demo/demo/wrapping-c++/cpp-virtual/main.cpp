#include <iostream>
#include "cpp_virt.h"

int main(int argc, char **argv)
{
    derived1 d1;
    derived2 d2;

    std::cout << "d1.call_frob(10) " << d1.call_frob(10) << std::endl;
    std::cout << "d2.call_frob(20) " << d2.call_frob(20) << std::endl;

    return 0;
}
