#############################################################################
# rect_6.py
#
# 1. Specifying a default view.
# 2. Defining a view item as readonly.
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, Property
from traitsui.api import View, Item, HGroup, VGroup
from traitsui.menu import OKCancelButtons

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits.
        Specify default values for the traits.
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
    traits_view = View('width', 'height', Item('area', style='readonly'),
                       resizable=True)
    
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
rect = Rectangle(width=3.0, height=4.0)
rect.edit_traits()

view1 = View(
             VGroup(
                    HGroup(
                           Item('width',label='w'),
                           Item('height', label='h')
                    ),
                    Item('area', style='readonly'),
            ),
            buttons=OKCancelButtons,
        )         
        
rect.edit_traits(view1)
