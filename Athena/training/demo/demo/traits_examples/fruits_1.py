#############################################################################
# Example showing how to use items from one trait as the drop-down choices
# in another.
#
# This version uses a list traits to provide the drop-down choices.
#
#############################################################################

from traits.api import HasTraits, Str, Property, List
from traitsui.api import View, Item, EnumEditor


class FruitPicker(HasTraits):
    
    # The 
    chosen_fruit = Str
    
    # List of available fruits
    available_fruits = List(Str)
    
        
    view = View( Item('chosen_fruit', 
                      editor=EnumEditor(name='available_fruits')
                     )
               )
    
#############################################################################
# Demo code
#############################################################################
    
fruit_picker = FruitPicker()

fruit_picker.available_fruits = ["orange","apple"]
fruit_picker.chosen_fruit = "orange"

fruit_picker.edit_traits()