#############################################################################
# ex_rect_2.py
#
# 1. Specifying Default values
#############################################################################

# enthought imports
from traits.api import HasTraits, Float

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits.
        Specify default values of 1.0 for the two traits.
    """
    
    # Width of the rectangle
    width = Float(1.0)
    
    # Height of the rectangle
    height = Float(2.0)


#############################################################################
# Demo Code
#############################################################################

rect = Rectangle()
print 'default rectangle width(1.0):', rect.width
print 'default rectangle height(2.0):', rect.height

# Using keyword arguments to initialize traits.
rect = Rectangle(width=2.0, height=3.0)
print 'keyword intialized rectangle width(2.0):', rect.width
print 'keyword initialized rectangle height(3.0):', rect.height


    