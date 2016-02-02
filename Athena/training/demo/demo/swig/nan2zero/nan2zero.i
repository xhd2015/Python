%module nan2zero

%{
#define SWIG_FILE_WITH_INIT
#include "nan2zero.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

// numpy typemaps.
// We want nan_to_zero_double() and nan_to_zero_float() to operate
// in-place, so we use the INPLACE_ARRAY1 typemap signature.
%apply (int DIM1, double *INPLACE_ARRAY1) {(int len, double *array)}
%apply (int DIM1, float *INPLACE_ARRAY1) {(int len, float *array)}

%include "nan2zero.h"
