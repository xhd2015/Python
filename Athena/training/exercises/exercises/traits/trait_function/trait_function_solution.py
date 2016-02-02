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

"""

from traitsui.api import View, Item
from traits.api import HasTraits, Float, Property, Array
from numpy import linspace, exp, set_printoptions, get_printoptions
from traitsui.api import RangeEditor, ArrayEditor


# 1. Create class that updates y whenever a, b,c or x change.

class Exponential(HasTraits):

    # Amplitude.
    a = Float(2.0)

    # Exponential decay constant.
    b = Float(0.76)

    # Offset.
    c = Float(1.0)

    # Values at which to evaluate the function.
    x = Array

    # The values of the functions at `x`.
    y = Property(depends_on=['a', 'b', 'c', 'x'])

    def _get_y(self):
        y = self.a * exp(-self.b * self.x) + self.c
        return y

    def _x_default(self):
        return linspace(0.0, 5.0, 6)


func = Exponential()
print func.y


# 2. Define a function `printer(value)` that prints an array, and set
#    it to be an external trait listener for the trait *y*.

def printer(value):
    opt = get_printoptions()
    set_printoptions(precision=2)
    print 'new value:', value
    set_printoptions(**opt)


func.on_trait_change(printer, name='y')
func.a = 2.1


# 3. Create a UI that displays a, b, and c as text boxes.
simple_view = View('a', 'b', 'c')
func.edit_traits(view=simple_view)

# 4. Create a UI that displays a, b, and c as sliders, and x and y
#    using ArrayEditors.
slider_view = View(Item('a', editor=RangeEditor(low=0.0, high=10.0)),
                   Item('b', editor=RangeEditor(low=0.0, high=10.0)),
                   Item('c', editor=RangeEditor(low=0.0, high=10.0)),
                   Item('x', style='readonly', editor=ArrayEditor(width=120)),
                   Item('y', style='readonly', editor=ArrayEditor(width=120)),
                   resizable=True,
              )
func.edit_traits(view=slider_view)
