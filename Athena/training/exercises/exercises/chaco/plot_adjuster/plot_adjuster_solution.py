"""
Plot adjuster
-------------

In this problem you will create a Figure containing a combination of
a line plot and a scatter plot, both using the same data.

In addition, the plot should be exposed together with Editors
that allow you to:

1. select from a sequence of functions to be plotted
2. change the color of the scatter-plot markers
3. change the background color of the plot (ColorTrait)
4. change the marker size (using a RangeEditor)
5. change the marker type (marker_trait)

Bonus
~~~~~
1. add User-Interface elements to allow changing the x-range and the
   number of data-points

See: :ref:`plot-adjuster-solution`.

"""

from numpy import linspace, cos, sin
from scipy.special import jn
from functools import partial

j0 = partial(jn, 0)
j1 = partial(jn, 1)
j2 = partial(jn, 2)

from enable.api import ColorTrait, ComponentEditor
from chaco.api import ArrayPlotData, Plot, marker_trait
from traits.api import Enum, HasTraits, Instance, Int, on_trait_change
from traitsui.api import Item, View, RangeEditor, HGroup, spring


class Adjuster(HasTraits):
    plot = Instance(Plot)
    color = ColorTrait("blue")
    marker = marker_trait
    marker_size = Int(4)
    function = Enum("j0", "j1", "j2", "cos", "sin")
    # Fixme:  This should probably be
    # function = Enum(j0, j1, j2, cos, sin)
    # but I don't know how to create the Editor to display
    # the right text in the drop down.

    xleft = Int(-14)
    xright = Int(14)
    num_points = Int(100)
    traits_view = View(
        Item('color', label="Color", style="custom"),
        Item('marker', label="Marker"),
        Item('marker_size', label="Size", editor=RangeEditor(low=1, high=20)),
        Item('function', label="Y data"),
        Item('plot', editor=ComponentEditor(), show_label=False),
        HGroup(spring, Item('xleft', label='min'),
               spring, Item('num_points', label='N'),
               spring, Item('xright', label='max'),
               spring
               ),
        width=800, height=650, resizable=True,
        title="Select All")

    def _plot_default(self):
        x = linspace(self.xleft, self.xright, self.num_points)
        y = j0(x)
        # Create the data and the PlotData object
        plotdata = ArrayPlotData(x=x, y=y)

        # Create a Plot and associate it with the PlotData
        plot = Plot(plotdata)
        plot.plot(('x', 'y'), type='line', color='red')
        # Create a line plot in the Plot
        self.renderer = plot.plot(("x", "y"), type="scatter", color="blue")[0]
        return plot

    def _function_changed(self, old, new):
        func = eval(self.function)
        xdata = self.plot.data.get_data("x")
        self.plot.data.set_data("y", func(xdata))

    def _color_changed(self):
        self.renderer.color = self.color

    def _marker_changed(self):
        self.renderer.marker = self.marker

    def _marker_size_changed(self):
        self.renderer.marker_size = self.marker_size

    @on_trait_change('xleft, xright, num_points')
    def _xdata_update(self):
        xdata = linspace(self.xleft, self.xright, self.num_points)
        self.plot.data.set_data("x", xdata)
        func = eval(self.function)
        ydata = func(xdata)
        self.plot.data.set_data("y", ydata)


# ==============================================================================
# demo object that is used by the demo.py application.
# ==============================================================================
demo = Adjuster()

if __name__ == "__main__":
    demo.configure_traits()
