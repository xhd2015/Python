// Define the modules name
%module example2

// Specify code that should be included at top of wrapper file.
%{
	#include "vect.h"
%}

// Define interface. Easy way out - Simply include the header
// file and let SWIG figure everything out.
%include "vect.h"
