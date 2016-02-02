#############################################################################
# configure_ui_2.py
#
# !! Run outside of a shell -- this will hang IPython...
# 1. Custom Views
# 2. Horizontal group layout
# 3. Setting the title of the dialog
# 4. Help messages.
#############################################################################

# enthought imports
from traitsui.api import View, Item, HGroup
from traits.api import HasTraits, Str, Int, Enum

class SimpleEmployee(HasTraits):
    
    first_name = Str(desc='First name of the Employee')
    last_name = Str
    gender = Enum('male', 'female')

    view = View(
                HGroup(
                       Item('first_name',label='First', resizable=True,
                            help='First name of the Employee',
                            ),
                       Item('last_name',label='Last',resizable=True,
                            help='Last name of the Employee',
                            ),
                       show_border=True,
                       label='Name',
                       ),
                Item('gender', help='Gender of the Employee'),
                resizable=True,
                title = "Employee",
                )       

#############################################################################
# Demo Code
#############################################################################

sam = SimpleEmployee()
sam.configure_traits()    
