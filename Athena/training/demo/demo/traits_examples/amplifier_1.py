#############################################################################
# amplifier_1.py
#
# 1. Static trait notifier.
#############################################################################

# enthought imports
from traits.api import HasTraits, Range

class Amplifier(HasTraits):
    """ Guitar Amplifier Model
    """
    
    # Volume setting for the amplifier.
    volume = Range(0.0, 11.0, value=5.0)

    #########################################################################
    # Protected interface
    #########################################################################    

    # static trait observers ################################################

    def _volume_changed(self, old, new):
        if new == 11.0:
            print "This one goes to eleven"


        
#############################################################################
# Demo Code
#############################################################################    

# This one goes to eleven...
spinal_tap = Amplifier()
spinal_tap.volume = 11.0
# It should print: This one goes to eleven
spinal_tap.volume = 11.0
# This won't print again because the value hasn't changed.
                   
