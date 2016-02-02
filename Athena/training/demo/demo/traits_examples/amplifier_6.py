#############################################################################
# amplifier_6.py
#
# 1. Synchronized traits
#############################################################################

# enthought imports
from traits.api import HasTraits, Range

# A re-usable trait for specifying volumes
volume_trait = Range(0.0, 11.0, value=5.0)

class Amplifier(HasTraits):
    """ Guitar Amplifier Model
    """
    
    # Volume setting for the amplifier.
    volume = volume_trait

    #########################################################################
    # Protected interface
    #########################################################################
    
    # static listeners ######################################################
    
    def _volume_changed(self, old, new):
        print "amplifier volume:", new
        
class ControlPanel(HasTraits):
    """ A control panel for the band
    """
    
    # Setting for the guitar volume
    guitar_volume = volume_trait
    
    # Setting for the microphone volume
    microphone_volume = volume_trait

    #########################################################################
    # Protected interface
    #########################################################################
    
    # static listeners ######################################################

    def _guitar_volume_changed(self, old, new):
        print "control panel guitar volume:", new
        
#############################################################################
# Demo Code
#############################################################################    

guitar_amplifier = Amplifier()
control_panel = ControlPanel()

# set up bi-directional synchronization
print "About to synchronize values"
control_panel.sync_trait('guitar_volume', guitar_amplifier, 'volume')

control_panel.guitar_volume = 1.0