#############################################################################
# rect_5.py
#
# 1. Specifying the dependencies of a Property with the 'depends_on' argument.
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, Property \
#, cached_property

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits.
        Specify default values of 1.0 for the two traits.
    """
    
    #########################################################################
    # Rectangle traits
    #########################################################################

    # Width of the rectangle
    width = Float(1.0)
    
    # Height of the rectangle
    height = Float(2.0)

    # The area of the rectangle (width*height)
    area = Property(depends_on=['width','height'])
    
    
    #########################################################################
    # Rectangle interface
    #########################################################################
    
    # Property get/set methods ##############################################
#    @cached_property
    def _get_area(self):
        """ Return the area (width*height) of the rectangle.
        """
        return self.width * self.height

        
#############################################################################
# Demo Code
#############################################################################        
rect = Rectangle(width=3.0, height=4.0)

