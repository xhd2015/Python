#include "Python.h"
#include "fact.h"

static PyObject* wrap_fact(PyObject *self, PyObject *args) 
{
    int n, result;
    /* Python->C Conversion */
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    
    /* Call our function */
    result = fact(n);
    
    /* C->Python Conversion */
    return Py_BuildValue("i", result);
}

static PyMethodDef ExampleMethods[] = {
    {"fact",  wrap_fact, METH_VARARGS, "Calculate the factorial of n"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initexample(void)
{
    (void) Py_InitModule("example", ExampleMethods);
}
