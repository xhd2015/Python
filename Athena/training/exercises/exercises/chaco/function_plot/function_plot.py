"""
Function Plot
-------------

The module `damped_osc.py` defines DampedOsc, a class that implements
the function::

     y = a * exp(-b * x) * cos(omega * x + phase).

It has four Float traits (`a`, `b`, `omega` and `phase`), an Array
trait (`x`), and a Property trait (`y`) that is an array computed
by the class.

The goal of this exercise is to create a view of a DampedOsc instance
that plots the function in a Chaco plot and allows the user to change
the parameters `a`, `b`, `omega` and `phase` using sliders.

The code is started for you.  This file may be run (from within ipython)
and a plot will be created with a slider below it for the parameter `a`.
However, the plot will not respond correctly to changes in `a`.
The following steps will lead to a working function plotter.

1. The class DampedOscView is started for you below, but it does not
   work correctly.  If you change `a` with the slider, the limits of
   the vertical axis change (this is done in the method _a_changed()),
   but the graph of the function does not reflect the new parameter.
   The problem is that the value of `y`, stored in the plot's
   ArrayPlotData instance, does not change when `a` changes.

   To fix this, add a static listener method, _y_changed(...), that
   updates the values of `y` in the plot's ArrayPlotData instance
   whenever the model's value of `y` changes.  You can get the plot's
   ArrayPlotData as self.plot.data, and you can use the ArrayPlotData
   method set_data(...) to update the value of `y`.

   Once you have made this change to the code, when the `a` slider
   is changed, you will see the vertical axis labels change, but
   the graph will appear unchanged, because now the change in the
   vertical axis matches the scale of the graph.

2. DampedOscView does not expose all the parameters of the model.
   Add a DelegatesTo trait for `b`.  Then in the View(), add an
   Item for `b`.  Use a RangeEditor (as in the Item for `a`), but
   use a range of 0 <= `b` <= 2.

   If you run the script after making the change, you should see
   that changing `b` with the slider automatically updates the
   graph.  (Why?)

3. Complete the function plotter by repeating the previous step
   for the parameters `omega` and `phase`.  Use the ranges::

       0 <= omega <= 10
       -pi <= phase <= pi

See :ref:`function-plot-solution`.

Note
~~~~
Take a look at `function_plot_solution2.py`, `function_plot_solution3.py`
and `function_plot_solution4.py`.  These solutions take advantage of
different Traits UI features to implement the function plotter.
"""

from math import pi

from traits.api import HasTraits, Instance, DelegatesTo
from traitsui.api import View, Item, RangeEditor, UItem, Group
from enable.api import ComponentEditor
from chaco.api import Plot, ArrayPlotData

# Local import
from damped_osc import DampedOsc


class DampedOscView(HasTraits):
    """
    Access the model using DelegatesTo().
    """

    model = Instance(DampedOsc)

    x = DelegatesTo('model')
    y = DelegatesTo('model')
    a = DelegatesTo('model')

    # Add delegated traits for the remaining DampedOsc traits...


    # The Plot instance that will show the graph of the function.
    plot = Instance(Plot)

    traits_view = \
        View(
            Group(
                UItem('plot', editor=ComponentEditor(), style='custom'),
            ),
            Item('a', label='a', editor=RangeEditor(low=0.0, high=10.0)),
            # Add additional Items here so the user can change b, omega,
            # and phase with sliders...

            # The following completes the definition of the View.
            resizable=True,
            width=600,
            height=550,
            title="a * exp(-b*x) * cos(omega*x + phase)",
        )

    def _plot_default(self):
        data = ArrayPlotData(x=self.x, y=self.y)
        plot = Plot(data)
        plot.plot(('x', 'y'), style='line', color='green')
        plot.value_range.set_bounds(-self.a, self.a)
        return plot

    def _a_changed(self):
        self.plot.value_range.set_bounds(-self.a, self.a)


if __name__ == "__main__":
    osc = DampedOsc()
    osc_viewer = DampedOscView(model=osc)
    osc_viewer.edit_traits()
