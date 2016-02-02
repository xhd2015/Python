#############################################################################
# ex_traffic_light_12.py
#
# 1. Default initialization
# 2. Enumerated editor
#############################################################################

# enthought imports
from traits.api import HasTraits, Enum


class TrafficLight(HasTraits):
    """ Model of a traffic light. 
    """
    
    # The color of the light 
    color = Enum("green", "yellow", "red")
        
#############################################################################
# Demo Code
#############################################################################    

def main():
    light = TrafficLight()
    print "default color of a traffic light:", light.color
    
    light = TrafficLight(color="red")
    print "set the initial color to 'red':", light.color
    
    light.color = "green"
    print light.color
    
    print "THIS WILL RAISE AN EXCEPTION"
    light.color = "blue"

if __name__ == "__main__":
    main()
