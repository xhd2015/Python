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
    xleft = Int(-14)
    xright = Int(14)
    num_points = Int(100)

    def _plot_default(self):
        pass

    def _function_changed(self, old, new):
        pass

    def _color_changed(self):
        pass

    def _marker_changed(self):
        pass

    def _marker_size_changed(self):
        pass

#==============================================================================
# demo object that is used by the demo.py application.
#==============================================================================
demo = Adjuster()


if __name__ == "__main__":
    demo.configure_traits()
