/*
 *  Example of embedding Python in another program.
 *
 *  Notes:
 *  1.  This C application runs fixed python code with PyRun_SimpleString().
 *  2.  The program also imports the module 'userscript'.  It does this with
 *      the function PyImport_ImportModule() from the Python C API.  This means
 *      that the file userscript.py must be in the import search path.  The
 *      programs adds the current directory to the python search path to
 *      make this work.  (A more flexible program would probably allow the
 *      user to select a file to be imported, and would therefore require
 *      some modifications to be able to import from an arbitrary path.)
 *  3.  THe program creates an extension module called 'tools'.  It uses the
 *      the same mechanism as used to wrap an external C library to be used
 *      in python.
 */

#include "Python.h"
#include <stdio.h>

void inittools(void); /* Forward */


int
main(int argc, char **argv)
{
    PyObject *pModule, *pResult;
    double result;

    /* Initialize the Python interpreter. */
    Py_Initialize();

    /*
     *  Add a static module. The 'tools' module will be available to
     *  the embedded Python interpreter to call back into the C application.
     */
    inittools();

    /* Do some application specific code */
    printf("\nThis is the C application.\n");
    printf("The following will be from the embedded Python interpreter.\n");
    printf("\n");

    /* Execute some Python statements (in module __main__) */
    PyRun_SimpleString("import random\n");
    PyRun_SimpleString("print '=== From embedded python! random =', random.random()\n");
    PyRun_SimpleString("import tools\n");
    PyRun_SimpleString("print '=== The meaning of life:', tools.meaning()\n");
    PyRun_SimpleString("print '=== fact(5) =', tools.fact(5)\n");
    printf("\n");

    printf("The C application is importing the 'userscript' module.\n\n");
    /*
     *  Add the current directory to the interpreter import search path,
     *  so we can import the local script from the directory where we are
     *  running.
     */
    PyRun_SimpleString("import sys\nsys.path.append('.')\n");

    /* import userscript */
    pModule = PyImport_ImportModule("userscript");

    printf("\n");

    /*
     *  Try to get the value of 'result' from userscript.  We expect it to
     *  be a Python float (i.e. C double precision).
     */
    if (pModule) {
        pResult = PyObject_GetAttrString(pModule, "result");
        if (pResult) {
            if (PyFloat_Check(pResult)) {
                result = PyFloat_AsDouble(pResult);
                printf("'userscript' defined result = %8.5f\n", result);
            } else {
                printf("result is not a floating point number!\n");
            }
            Py_DECREF(pResult);
        } else {
            printf("The 'userscript' module did not define 'result'.\n");
        }
        Py_DECREF(pModule);
    } else {
        printf("Failed to import 'userscript'.\n");
    }

    printf("\nThe C application is exiting.\n\n");

    /* Exit, cleaning up the interpreter */
    Py_Exit(0);
}

/*
 *  The following code sets up the extension module that will allow python
 *  code run by the embedded intepreter to access functions defined in this
 *  C file.  The extension module will be the 'tools' module.
 */

int
fact(int n)
{
    if (n <= 1)
        return 1;
    else
        return n * fact(n - 1);
}

/*
 *  tools_meaning will be callable from python, but it does not wrap an
 *  an exsiting C function.  It simply returns 42.
 */
static PyObject *
tools_meaning(PyObject *self, PyObject* args)
{
    return PyInt_FromLong(42L);
}

/*
 *  tools_fact is the wrapper for the fact() function.
 */
static PyObject*
tools_fact(PyObject *self, PyObject *args) 
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

static PyMethodDef tools_methods[] = {
    {"meaning", tools_meaning, METH_NOARGS, "Return the meaning of everything."},
    {"fact", tools_fact, METH_VARARGS, "Calculate the factorial of n."},
    {NULL, NULL, 0, NULL}           /* sentinel */
};

void
inittools(void)
{
    /* Initialize the 'tools' module. */
    PyImport_AddModule("tools");
    Py_InitModule("tools", tools_methods);
}
