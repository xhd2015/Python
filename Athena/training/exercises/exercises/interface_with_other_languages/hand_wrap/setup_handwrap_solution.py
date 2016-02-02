"""
Fancy science (hand wrap)
-------------------------

This exercise provides practice at writing a C extension module
"by hand."   That is, you will write all the interface code yourself
instead of using a tool such as SWIG.

``fancy_science.h`` and ``fancy_science.c`` are the header and implementation file
for a *very* simple library that contains three functions::

    /* Calculate the hypotenuse of a triangle using the Pythagorean theorem */
    double my_hypot(double a, double b);

    /* Calculate Euler's number, e, using n series elements. */
    double eulers_number(int n);
    
    /* Einstein's e=mc^2 calculation */    
    float energy(float mass)
    
In this exercise, you will wrap these functions and expose them to 
Python through an extension module.  The skeleton for this module,
``func_module.c`` already exists, and the first function, ``my_hypot``,
has already been wrapped for you.

There is a ``setup_handwrap.py`` file that is the Python equivalent of a "make" file.  
To build the extension on Windows using the mingw compiler and so
that the resulting module is put in this directory instead of a separate
build directory, do the following::

    c:\path\exercise\> setup_handwrap.py build_ext --compiler=mingw32 --inplace 

The ``build.bat`` file has this command in it already for convenience, so 
you can also build the module by typing::

    c:\path\exercise\> build.bat
    
To test the module, import it from the Python command interpreter and
call its functions.  The following will work "out of the box."::
    
    c:\path\exercise\> python
    >>> import fancy_science
    >>> fancy_science.my_hypot(3.0, 4.0)
    5.0    


Help
~~~~

The demo directory has a more detailed example of the ``my_hypot`` function 
that may be useful.  See the file ``readme.txt`` in that directory to see how
to build the examples.

The python documentation on building extensions is here:

    http://docs.python.org/ext/ext.html


The format strings for parsing tuples is here:

    http://www.python.org/doc/1.5.2p2/ext/parseTuple.html
    
For more information about writing setup.py files, look here:

    http://docs.python.org/inst/inst.html

"""

from distutils.core import Extension, setup

ext = Extension(name="fancy_science",
                sources=['fancy_science.c', 'fancy_science_solution.c'],
                include_dirs=['.'])

if __name__ == '__main__':
    setup(name='fancy_science',
          version='1.0',
          ext_modules=[ext])                
