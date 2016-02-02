#############################################################################
# rect_4.py
#
# 1. Read-only Property
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, Property

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits.
        Specify default values of 1.0 for the two traits.
    """
    
    # Width of the rectangle
    width = Float(1.0)
    
    # Height of the rectangle
    height = Float(2.0)

    # The area of the rectangle (width*height)
    area = Property
    
    #########################################################################
    # Protected interface
    #########################################################################
    
    # Property get/set methods ##############################################
    
    def _get_area(self):
        """ Return the area (width*height) of the rectangle.
        """
        return self.width * self.height

        
#############################################################################
# Demo Code
#############################################################################    

rect = Rectangle(width=2.0, height=3.0)
print 'default rectangle width(2.0):', rect.width
print 'default rectangle height(3.0):', rect.height
print 'rectangle area (6.0):', rect.area
print 'rectangle.width = 4.0'
rect.width = 4.0
print 'rectangle area (12.0):', rect.area
