

%module(directors="1") cpp_virt
%{
#include "cpp_virt.h"
%}

%feature("director");

%include "cpp_virt.h"
