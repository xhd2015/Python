%module rms

%{
#define SWIG_FILE_WITH_INIT
#include "rms.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

// Basic typemap for an array and its length.  It is essential that the
// signature in curly braces match the signature of the `rms()` function
// arguments **exactly**.
%apply (double* IN_ARRAY1, int DIM1) {(double* seq, int n)}

// The above typemap is applied to the rms() function signature.
%include "rms.h"

// vim:ft=cpp
