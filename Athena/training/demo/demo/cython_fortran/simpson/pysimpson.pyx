cdef extern:
    double c_simpson(double (*f)(double *), double *a, double *b, int *n)

_callback_function_stack = []

cdef double callback(double *x):
    global _callback_function_stack
    cdef double value, result
    value = x[0]
    result = _callback_function_stack[-1](value)
    return result

def simpson(f, double a, double b, int n):
    global _callback_function_stack

    # Sanity check of the callback:
    # Make an initial call f(a), and verify it returns a number.
    test = f(a)
    if not isinstance(test, float):
        try:
            test = float(test)
        except TypeError:
            raise TypeError("return value of f is not a number")

    _callback_function_stack.append(f)
    result = c_simpson(callback, &a, &b, &n)
    _callback_function_stack.pop()
    return result
