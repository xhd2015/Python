#############################################################################
# water_tank_2.py
#
# 1. property with trait validation
#############################################################################

# enthought imports
from traits.api import HasTraits, Float, Property


class WaterTank(HasTraits):
    """ A water tank has a height and a water level.  The water level can
        not exceed the height of the tank.
    """
    
    # The level of the water in the Tank.
    # The value passed in must be a Float.
    water_level = Property(Float)
    
    # A "shadow" trait to store the actual water_level
    _water_level = Float(0.0)
    
    # Height of the water tank -- the water level can't be higher than this.
    height = Float(100.0)
    
    #########################################################################
    # Protected interface
    #########################################################################
    
    # Property get/set methods ##############################################
    
    def _get_water_level(self):
        """ Return the _water_level value
        """
        return self._water_level
        
    def _set_water_level(self, value):
        """ Set the water level.  This must be less than the tank height.
        """
        if value < self.height:
            self._water_level = value
        else:
            self._water_level = self.height
            # Or you might choose to raise an error.
            #raise ValueError, "The water level must be less than the height"
        
        
#############################################################################
# Demo Code
#############################################################################    

def main():
    water_tank = WaterTank()
    print "The tank height is:", water_tank.height 
    water_tank.water_level = 110.0
    print "Set water_level to 110. It should clip to 100.:", \
          water_tank.water_level
    
    # Now this raises a trait error because "hello" isn't coercable to float.
    print "THIS WILL RAISE AN EXCEPTION"
    water_tank.water_level = "hello"
    print water_tank.water_level

if __name__ == "__main__":
    main()
