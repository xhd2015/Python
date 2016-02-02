#############################################################################
# amplifier_3.py
#
# 1. Dynamic notifiers use weak references to methods.
#############################################################################

# enthought imports
from traits.api import HasTraits, Range


class Amplifier(HasTraits):
    """ Guitar Amplifier Model
    """

    # Volume setting for the amplifier.
    volume = Range(0.0, 11.0, value=5.0)

class Listener(object):

    def printer(self, value):
        """ Observer function that I'll connect to listen for trait changes.
        """

        print "new value:", value


#############################################################################
# Demo Code
#############################################################################    

spinal_tap = Amplifier()

listener = Listener()

# Connect the dynamic observer
spinal_tap.on_trait_change(listener.printer, name='volume') 
spinal_tap.volume = 11.0
# "new value: 11.0" is printed

# del the listener object, and the notifier will not be called.
del listener
spinal_tap.volume = 10.0
# nothing is printed
