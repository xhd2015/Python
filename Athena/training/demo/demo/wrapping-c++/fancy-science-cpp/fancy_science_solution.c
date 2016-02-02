/****************************************************************************
  Include the Python.h header file so that we can use its data structures.
 ***************************************************************************/
#include "Python.h"
#include "fancy_science.h"

/****************************************************************************
  Our simple hypot function that can be called from python.
 ***************************************************************************/

static PyObject *
my_hypot_wrapped(PyObject *self, PyObject *args)
{
    double a, b, c;

    if (!PyArg_ParseTuple(args, "dd:my_hypot", &a, &b))
    {
        return NULL;
    }
    
    c = my_hypot(a,b);
    
    return Py_BuildValue("d", c);
}

static PyObject *
eulers_number_wrapped(PyObject *self, PyObject *args)
{
    double e;
    int n;

    if (!PyArg_ParseTuple(args, "i:eulers_number", &n))
    {
        return NULL;
    }
    
    e = eulers_number(n);
    
    return Py_BuildValue("d", e);
}

static PyObject *
energy_wrapped(PyObject *self, PyObject *args)
{
    float mass, e;

    if (!PyArg_ParseTuple(args, "f:energy", &mass))
    {
        return NULL;
    }
    
    e = energy(mass);
    
    return Py_BuildValue("f", e);
}

/****************************************************************************
  Declare a list of the python functions this module exports to python. 
 ***************************************************************************/

static PyMethodDef HypotMethods[] = {
    {"my_hypot",  my_hypot_wrapped, METH_VARARGS,
     "Calculate the hypotenuse of a right triangle given its two sides."},
    {"eulers_number",  eulers_number_wrapped, METH_VARARGS,
     "Calculate Euler's number, e, using n series elements."},
    {"energy",  energy_wrapped, METH_VARARGS,
     "Given mass (kg), calculate energy (joules) given Einstein's famous e=mc^2."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


/****************************************************************************
  Initialize the module.  This is the *only* non-static method in the file.
 ***************************************************************************/

PyMODINIT_FUNC
initfancy_science(void)
{
    (void) Py_InitModule("fancy_science", HypotMethods);
}
