
from traits.api import (HasTraits, Instance)
from traitsui.api import (View, Item)
from enable.api import ComponentEditor
from chaco.api import Plot, ArrayPlotData, jet

import numpy as np

class PlotBase(HasTraits):
    plot = Instance(Plot)

    traits_view = View(
            Item('plot', editor=ComponentEditor(), show_label=False),
            width=500,
            height=500,
            resizable=True,
            title="Chaco Plot")

class LinePlot(PlotBase):

    def _plot_default(self):
        x = np.linspace(-14, 14, 100)
        y = np.sin(x) * x**3
        plotdata = ArrayPlotData(x=x, y=y)

        plot = Plot(plotdata)
        plot.plot(('x', 'y'), type='line', color='blue')
        plot.title = 'sin(x) * x^3'
        return plot

class ImagePlot(PlotBase):

    def _plot_default(self):
        x = np.linspace(0, 10, 51)
        y = np.linspace(0, 5, 51)
        X, Y = np.meshgrid(x, y)
        z = np.exp(-(X**2 + Y**2) / 100)
        plotdata = ArrayPlotData(zdata=z[:-1, :-1])
        plot = Plot(plotdata)
        plot.img_plot("zdata", xbounds=x, ybounds=y, colormap=jet)
        return plot


if __name__ == '__main__':
    lp = LinePlot()
    lp.configure_traits()
    ip = ImagePlot()
    ip.configure_traits()
