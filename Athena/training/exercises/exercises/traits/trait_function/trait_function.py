""" 
Trait Function
--------------

Traits-based class for calculating a function.

1. Write a Traits-based class that calculates the following signal::

       y = a*exp(-b*x) + c

   Make *a*, *b*, and *c* floating point traits with default
   values of 2.0, 0.76, 1.0. The *x* variable should be an array
   trait with the default value [0, 0.5, 1, 1.5, ..., 5.0].
   The *y* value should be a property trait that updates any time
   *a*, *b*, *c* or *x* changes.

   Once your class is defined, create an instance of the object and
   print its *y* value.

2. Define a function `printer(value)` that prints an array, and set
   it to be an external trait listener for the trait *y* on the
   instance created in 1, so *y*'s value it printed whenever it
   changes.

3. Create a UI that displays *a*, *b*, and *c* as text boxes.

4. Create a UI that displays *a*, *b*, and *c* as sliders,
   and *x* and *y* as read-only arrays.  Use an ArrayEditor for the
   display of the arrays, and set the 'width' keyword of the
   ArrayEditor to a value large enough for the values in the array.

See: :ref:`trait-function-solution`.
"""

from traitsui.api import View, Item
from traits.api import HasTraits, Float, Property, Array
from numpy import linspace, exp, set_printoptions
from traitsui.api import RangeEditor


# 1. Create class that updates y whenever a, b, c or x change.

class Exponential(HasTraits):
    
    # Amplitude.
    a = Float(2.0)

    # Fill in your code here.    


func = Exponential()        
#print func.y


# 2. Define a function `printer(value)` that prints an array, and set
#    it to be an external trait listener for the trait *y*.


# 3. Create a UI that displays a, b, and c as text boxes.

# Set up a view.
# simple_view = View(...)

# Use it for your traits.
# func.edit_traits(view=simple_view)


# 4. Create a UI that displays a, b, and c as sliders.
