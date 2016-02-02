"""  The default CheckboxColumn uses a round check/uncheck icon.
     This one provides more traditional square check/uncheck 
     boxes.  It also centers it in the column that it is in.
"""

# Enthought-library imports
from traitsui.extras.checkbox_column import CheckboxColumn
from traits.api import Dict
from pyface.image_resource import ImageResource

checked_image_map = { True: ImageResource('checked'),
                      False: ImageResource('unchecked'),
                    }

class SquareCheckboxColumn(CheckboxColumn):
    
    # This needs to be a copy, correct...
    image_map = Dict(checked_image_map)
    
    def __init__ ( self, **traits ):
        """ Initializes the object.
        """
        super( SquareCheckboxColumn, self ).__init__( **traits )
        self.renderer.renderer.image_map = self.image_map
        self.horizontal_alignment = 'center'
