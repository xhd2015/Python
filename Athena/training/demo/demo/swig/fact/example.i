// Define the modules name
%module example

// Specify code that should be included at top of wrapper
// file.
%{
	#include "fact.h"
%}

// Define interface. Easy way out - Simply include the
// header file and let SWIG figure everything out.
%include "fact.h"
