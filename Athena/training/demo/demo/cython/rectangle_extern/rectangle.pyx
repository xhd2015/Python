""" Cython wrapper around the cpp class defined inside rectangle_extern.cpp.

except + allows Cython to deal properly with errors inside the constructor.
"""


# This part only 'import' things from the .h code by adding a #include

cdef extern from "rectangle_extern.h" namespace "shapes":
    cdef cppclass Rectangle:
        Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getLength()
        int getHeight()
        int getArea()
        void move(int, int)

cdef class PyRectangle:
    """ Python visible class that exposes only 1 method and the attributes
    """
    cdef Rectangle *thisptr      # hold a C++ instance which we're wrapping
    cdef public int x0, y0, x1, y1
    def __cinit__(self, int x0, int y0, int x1, int y1):
        print "Creating the C++ rectangle object..."
        self.thisptr = new Rectangle(x0, y0, x1, y1)
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        
    def __dealloc__(self):
        print "deallocating..."
        del self.thisptr
        
    def getLength(self):
        return self.thisptr.getLength()
