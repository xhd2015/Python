This demo shows the basics of "wrapping" a C function so that
it is callable from Python.  The wrapped function is calculates
the hypotenuse of a right triangle given the length of its two sides.

There are actually 4 examples in this directory:

1. build_main.bat, main.c
   
   This builds a simple C program that that calculates the hypotenuse
   in its "main" routine.  Inspect the main.c file to see how you 
   could calculate the hypotenuse in pure C.
   
   Running the following commands should give the following results.
   
    c:\demo> build_main.bat
    c:\demo> main
    The hypotenuse of a triangle with sides 3.0 and 4.0 is 5.0.
         
2. build_main2.bat, main2.c, hypot.h, hypot.c
   
   This builds a simple C program that that calculates the hypotenuse
   by calling the function hypot().  This is intended to show a more
   typical approach of calling a function from a mathematical library.
   Inspect the hypot.h and hypot.c files respectively to see how you
   might create a hypotenuse calculating function in a library.Inspect 
   the main.c file to see how you can call this function.
   
   Running the following commands should give the following results.
   
    c:\demo> build_main2.bat
    c:\demo> main2
    The hypotenuse of a triangle with sides 3.0 and 4.0 is 5.0.

3. build_hypot.bat, hypot_module.c
      
   Build a simple Python function to calculate the hypotenuse.  The
   build_hypot.bat file will build the module by calling the compiler
   directly.  The main_python.py file will load your newly created 
   module, and call it from python.

    c:\demo> build_hypot.bat
    c:\demo> python
    >>> from hypot2 import my_hypot
    >>> my_hypot(3.0, 4.0)
    5.0
   
4. setup_hypot2.py, hypot2_module.c, hypot.h, hypot.c
   
   Build a simple Python function to calculate the hypotenuse.  The
   build_hypot2.bat file will build the module by calling the compiler
   directly.  
   
   The setup_hypot2.py file serves exactly the same purpose, but
   uses the standard python "build" tool.  You run the setup_hypot2.py
   file like this on windows:
   
    c:\demo> python setup_hypot2.py build --inplace --compiler=mingw32
    c:\demo> python
    >>> from hypot2 import my_hypot
    >>> my_hypot(3.0, 4.0)
    5.0
