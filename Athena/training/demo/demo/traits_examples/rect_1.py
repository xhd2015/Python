#############################################################################
# rect_1.py
#
# 1. Type Declaration 
# 2. Default initialization
# 3. Type casting
# 4. Type checking
#############################################################################

# enthought imports
from traits.api import HasTraits, Float

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits.
    """
    
    # Width of the rectangle
    width = Float
    
    # Height of the rectangle
    height = Float

#############################################################################
# Demo Main
#############################################################################

def main():

    # Default initialization
    rect = Rectangle()
    print 'default rectangle width (0.0):', rect.width
    
    # Set rect width to 1.0
    rect.width = 1.0
    print 'set rectangle width (1.0):', rect.width
    
    # Float traits will convert an integer
    rect.width = 2
    print 'set rectangle width with integer(2):', rect.width
    
    # But will throw an error when assigning string
    print "THIS WILL THROW EXCEPTION"
    rect.width = "1.0"
    print 'rectangle width:', rect.width

if __name__ == '__main__':
    main()    