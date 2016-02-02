#############################################################################
# amplifier_2.py
#
# 1. Dynamic trait notifier.
#############################################################################

# enthought imports
from traits.api import HasTraits, Range


class Amplifier(HasTraits):
    """ Guitar Amplifier Model
    """
    
    # Volume setting for the amplifier.
    volume = Range(0.0, 11.0, value=5.0)
    
def printer(value):
    """ Observer function that I'll connect to listen for trait changes.
    """
    
    print "new value:", value
        
        
#############################################################################
# Demo Code
#############################################################################    

spinal_tap = Amplifier()

# Connect the dynamic observer to a couple of traits
spinal_tap.on_trait_change(printer, name='volume') 
spinal_tap.volume = 11.0
spinal_tap.volume = 10.0

# Now disconnect it from volume.
spinal_tap.on_trait_change(printer, name='volume', remove=True)
spinal_tap.volume = 9.0