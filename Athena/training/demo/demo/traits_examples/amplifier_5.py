#############################################################################
# amplifier_5.py
#
# 1. on_trait_change listener on running on a different thread
#############################################################################

from time import sleep
import thread
from traits.api import HasTraits, Range


class Amplifier(HasTraits):
    """ Guitar Amplifier Model
    """
    
    # Volume setting for the amplifier.
    volume = Range(0.0, 11.0, value=5.0)

    def __init__(self, *args, **kw):
        super(Amplifier, self).__init__(*args, **kw)
        self.on_trait_change(self.update, 'volume', dispatch='new')

    def update(self, name, value):
        seconds = 3.0
        print 'thread identity %s sleeping for %s second' % \
               (thread.get_ident(), seconds)
        sleep(seconds)
        print 'trait %s updated to %s' % (name, value)
        
#############################################################################
# Demo Code
#############################################################################    

print 'main thread: %s' % thread.get_ident()
spinal_tap = Amplifier()

spinal_tap.volume = 11.0
