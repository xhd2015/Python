"""Example showing how to write a simple decorator.

The code below defines a decorator `logger` than can be applied to any
function.  When applied to a function, the decorated function prints
messages to standard output before the function is entered and after
it has exited, with details of the input arguments and the return
value or (if appropriate) the exception raised.

"""
import functools


def logger(func):
    """
    A logging decorator that prints messages to standard output when
    the decorated function is entered and when it's left.

    """

    # Create a wrapper function that calls the original.
    # Since we don't know the signature of the decorated function,
    # we use the general *args, **kwargs form.
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        func_name = func.__name__
        print "Entering {!r} with args={} and kwargs={}.".format(
            func_name, args, kwargs)
        try:
            # Call the wrapped function.
            result = func(*args, **kwargs)
        except Exception as e:
            print "{!r} raised an exception: {}.\n".format(func_name, e)
            raise
        else:
            print "Leaving {!r} with result {!r}.\n".format(func_name, result)
            return result

    # Return the wrapper function.
    return wrapper_func


# An example of applying this decorator to a simple function.

@logger
def sum(a, b):
    """
    Return the sum of a and b.

    """
    return a + b


# Now use the sum function in the normal way.
print sum(6, b=7)
sum(a=3, b=8)
