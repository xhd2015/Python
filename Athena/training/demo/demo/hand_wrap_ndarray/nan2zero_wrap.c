
#include "Python.h"
#include "numpy/arrayobject.h"

#include "nan2zero.h"


/*
 *  C wrapper for the functions nan_to_zero_double() and
 *  nan_to_zero_float().
 */

static PyObject *nan_to_zero_wrap(PyObject *dummy, PyObject *args)
    {
    PyObject *arg1 = NULL;
    int flags;
    int size;
    int itemsize;
    void *pdata;

    if (!PyArg_ParseTuple(args, "O!:nan_to_zero", &PyArray_Type, &arg1))
        return NULL;

    /* Check that arg1 is a ndarray with a float-point data type. */
    if (!PyArray_ISFLOAT(arg1))
        {
        PyErr_SetString(PyExc_ValueError, "nan_to_zero: numpy array must have a floating point type");
        return NULL;
        }

    /* Check that arg1 is a contiguous array. */
    flags = PyArray_FLAGS(arg1);
    if (!(flags & NPY_CONTIGUOUS))
        {
        PyErr_SetString(PyExc_ValueError, "nan_to_zero: numpy array must be contiguous");
        return NULL;
        }

    /*
     *  Figure out if arg1 is of type 'float' or 'double', and
     *  call the appropriate C function.
     */
    size = PyArray_SIZE(arg1);
    pdata = PyArray_DATA(arg1);
    itemsize = PyArray_ITEMSIZE(arg1);
    if (itemsize == sizeof(float))
        nan_to_zero_float(size, (float *) pdata);
    else
        nan_to_zero_double(size, (double *) pdata);

    Py_INCREF(Py_None);
    return Py_None;
    }

static PyMethodDef wrappers[] =
    {
        {"nan_to_zero", nan_to_zero_wrap, METH_VARARGS,
           "Convert all nans in a numpy array of floats to 0"},
        {NULL, NULL, 0, NULL}
    };

PyMODINIT_FUNC initnan2zero(void)
    {
    import_array();
    (void) Py_InitModule("nan2zero", wrappers);
    }
