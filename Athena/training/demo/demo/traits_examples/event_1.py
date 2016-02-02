#############################################################################
# ex_event.py
#
# 1. Use an event to externally manage updates.
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, Event

class Rectangle(HasTraits):
    """ Simple rectangle class with type declarations for two traits and
        an event. 
    """
    
    # Width of the rectangle
    width = Float(1.0)
    
    # Height of the rectangle
    height = Float(2.0)

    # Set to notify others that you have changed to a Rectangle
    # Listen to this if you want to react to any changes to a Rectangle
    updated = Event

def rect_printer(rect, name, value):
    print 'rectangle (width, height):', rect.width, rect.height
    
# Demo Code
rect = Rectangle()

# Hook up a dynamic listener to respond whenever rect is updated.
rect.on_trait_change(rect_printer, name='updated')

# update multiple items
rect.width = 10
rect.height = 20

# now explicitly tell the item that it is updated
rect.updated = True

