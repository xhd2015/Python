"""
Custom tool
-----------

In this exercise you will add custom interactivity to a Chaco plot by
creating a custom tool that allows a user to add new points by clicking.

1. Create a Chaco Plot that plots sin(x) * x**3 from -14 to 14
2. Create a Custom Tool that responds to mouse clicks and
    a) places a point on the plot at each clicked location and
    b) prints the location of the click to standard-out.

   Hint:  Add the clicked value to the data that is plotted.

Bonus
~~~~~

Add the ability to remove the point nearest the location that is
clicked.
"""

from numpy import linspace, sin, r_

from chaco.api import ArrayPlotData, Plot
from enable.api import BaseTool, ComponentEditor
from traits.api import HasTraits, Instance
from traitsui.api import Item, View


class CustomTool(BaseTool):

    def normal_left_down(self, event):
        # Map the screen-space coordinates back into data space
        new_x, new_y = self.component.map_data((event.x, event.y))
        print "Data:", new_x, new_y

        # Get a reference to the PlotData  (self.component is a Plot)
        plotdata = self.component.data

        # Get the index (x) and value (y) datasources
        x_ary = plotdata.get_data("x")
        y_ary = plotdata.get_data("y")

        # Set the new data arrays
        plotdata.set_data("x", r_[x_ary, new_x])
        plotdata.set_data("y", r_[y_ary, new_y])


class ScatterPlot(HasTraits):

    plot = Instance(Plot)

    traits_view = View(Item('plot', editor=ComponentEditor(),
                            show_label=False),
                       width=800, height=600, resizable=True,
                       title="Custom Tool")

    def _plot_default(self):
        # Create the data and the PlotData object
        x = linspace(-14, 14, 100)
        y = sin(x) * x**3
        plotdata = ArrayPlotData(x=x, y=y)
        # Create a Plot and associate it with the PlotData
        plot = Plot(plotdata)
        # Create a scatter plot in the Plot
        plot.plot(("x", "y"), type="scatter", color="blue")
        # Add our custom tool to the plot
        plot.tools.append(CustomTool(plot))
        return plot


demo = ScatterPlot()
if __name__ == "__main__":
    demo.configure_traits()
