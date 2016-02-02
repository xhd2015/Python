#include "cpp_virt.h"

base::base() : _base_double(10.0) {}

base::~base() {}

int base::frobnicate(int i)
{
    return 0;
}

int base::call_frob(int i)
{
    return this->frobnicate(i);
}

derived1::derived1() : _derived1_int(1) {}

derived1::~derived1() {}

derived2::derived2() : _derived2_int(2) {}

derived2::~derived2() {}

int derived1::frobnicate(int i)
{
    _derived1_int += i;
    return _derived1_int;
}

int derived2::frobnicate(int i)
{
    _derived2_int -= i;
    return _derived2_int;
}

