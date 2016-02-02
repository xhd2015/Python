from traits.api import (HasTraits, Instance)
from traitsui.api import (View, Item, Group)
from enable.api import ComponentEditor, Component
from chaco.api import Plot, ArrayPlotData, jet, VPlotContainer

import numpy as np

class Plots(HasTraits):

    composite_plot = Instance(Component)

    traits_view = View(
            Group(
                Item('composite_plot',
                    editor=ComponentEditor(),
                    show_label=False),
                orientation = "vertical"),
            resizable=True, title="Two Chaco Plots"
            )

    def _composite_plot_default(self):

        x_line = np.linspace(-14, 14, 100)
        y_line = np.sin(x_line) * x_line**3

        x = np.linspace(0, 10, 51)
        y = np.linspace(0, 5, 51)
        X, Y = np.meshgrid(x, y)
        z = np.exp(-(X**2 + Y**2) / 100)

        plotdata = ArrayPlotData(x=x_line, y=y_line, zdata=z[:-1, :-1])

        line_plot = Plot(plotdata)
        line_plot.plot(('x', 'y'), type='line', color='blue')

        img_plot = Plot(plotdata)
        img_plot.img_plot("zdata", xbounds=x, ybounds=y, colormap=jet)

        cp = VPlotContainer()
        cp.add(img_plot)
        cp.add(line_plot)
        return cp

if __name__ == '__main__':
    Plots().configure_traits()
