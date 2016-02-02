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

See: :ref:`custom-tool-solution`.
"""

from numpy import linspace, sin, r_

from chaco.api import ArrayPlotData, Plot
from enable.api import BaseTool, ComponentEditor
from traits.api import Enum, HasTraits, Instance
from traitsui.api import Item, View


class CustomTool(BaseTool):
    pass


class ScatterPlot(HasTraits):
    pass


demo = ScatterPlot()
if __name__ == "__main__":
    demo.configure_traits()
