/****************************************************************************
  Include the Python.h header file so that we can use its data structures.
 ***************************************************************************/
#include "Python.h"
#include <math.h>

/****************************************************************************
  Our simple hypot function that can be called from python.
 ***************************************************************************/

static PyObject *
my_hypot(PyObject *self, PyObject *args)
{
    double a, b, c;

    /* Unpack phase
    
       The *args object passed into this function by python is a tuple that
       holds the Python arguments from the Python function call.  For example,
       if the function in Python is called with:
       
          >>> hypot(3.0, 4.0)
          
       The first value in *args is 3.0 and 4.0.  PyArg_ParseTuple handles
       unpacking these values into our a and b variables.  The format 
       string "dd:hypot" says that the first and second variables should be
       unpacked as "doubles".  The "hypot" is a string used to report 
       the name of the offending function in case an error occurs during
       unpacking.
       
       If an error does occur while unpacking, we return NULL.  The Python
       interpreter recognizes this as an error and will throw an exception.       
       
       Note that the self argument is not used in functions (it will be
       NULL).  It is only used when writing class methods.
    */   
    if (!PyArg_ParseTuple(args, "dd:hypot", &a, &b))
    {
        return NULL;
    }
    
    /* Calculation phase.
    
       Calulate the hypotenuse.
    */   
    c = sqrt(a*a+b*b);
    
    /* Pack phase
    
       Now we need to convert the result (c) from a C double into a
       double percision floating point PyObject.
    */
    return Py_BuildValue("d", c);
}

/****************************************************************************
  Declare a list of the python functions this module exports to python. 
 ***************************************************************************/

static PyMethodDef HypotMethods[] = {
    {"my_hypot",  my_hypot, METH_VARARGS,
     "Calculate the hypotenuse of a right triangle given its two sides."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


/****************************************************************************
  Initialize the module.  This is the *only* non-static method in the file.
 ***************************************************************************/

PyMODINIT_FUNC
inithypot(void)
{
    (void) Py_InitModule("hypot", HypotMethods);
}
