#############################################################################
# rect_7.py
#
# 1. Specifying a default view.
# 2. Defining a view item as readonly.
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, Property
from traitsui.api import View, Item

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

    # Default User Interface view of object
    traits_view = View('width', 'height', Item('area', style='readonly'))

    #########################################################################
    # Rectangle interface
    #########################################################################

    # Property get/set methods ##############################################

    def _get_area(self):
        """ Return the area (width*height) of the rectangle.
        """
        return self.width * self.height


#############################################################################
# Demo Code
#############################################################################    
def printer(value):
    print 'The new area is:', value

rect = Rectangle()

# Thanks to the trait_property_changed() lines above, this function is
# called whenever the area of the rectanlge changes.
rect.on_trait_change(printer, 'area')

# printer should be called...
rect.width = 10
