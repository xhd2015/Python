#############################################################################
# configure_ui_1.py
#
# !! Run outside of a shell -- this will hang IPython...
# 1. Simple configure_traits() UI example
#############################################################################

# enthought imports
from traits.api import HasTraits, Str, Int, Enum

class SimpleEmployee(HasTraits):
    
    first_name = Str
    last_name = Str
    gender = Enum('male', 'female')

#############################################################################
# Demo Code
#############################################################################

sam = SimpleEmployee()
sam.configure_traits()    
