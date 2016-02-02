#############################################################################
# rect_3.py
#
# 1. Coercion vs. Casting
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, CFloat

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits.
        Specify default values of 1.0 for the two traits.
    """
    
    # Width of the rectangle
    # Basic traits (like Float) use coersion when assigning variables to
    # a trait.  Coersion allows "widening" of types (Int->Float), but
    # does not allow potentially problematic conversions. (Str->Float)
    width = Float
    
    # Height of the rectangle
    # Casting traits (like CFloat) will use Python's builtin float() method
    # to attempt to convert variables assigned to height.
    height = CFloat


def main():
    # Test the default value
    rect = Rectangle()
    
    rect.height = "2.0"
    print 'assigning string to CFloat height(2.0):', rect.height
    
    print "assigning string to Float -- THIS WILL THROW EXCEPTION"
    rect.width = "1.0"
    print 'rectangle width:', rect.width


if __name__ == '__main__':
    main()    