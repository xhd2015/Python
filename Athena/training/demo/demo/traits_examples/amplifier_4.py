#############################################################################
# amplifier_4.py
#
# 1. on_trait_change decorator
#############################################################################

# enthought imports
from traits.api import HasTraits, Range, on_trait_change


class Amplifier(HasTraits):
    """ Guitar Amplifier Model
    """
    
    # Volume setting for the amplifier.
    volume = Range(0.0, 11.0, value=5.0)
    
    reverb = Range(0, 10.0, value=5.0)

    @on_trait_change('reverb, volume')
    def update(self, name, value):
        print 'trait %s updated to %s' % (name, value)
        
#############################################################################
# Demo Code
#############################################################################    

spinal_tap = Amplifier()

spinal_tap.volume = 11.0
spinal_tap.reverb = 2.0
