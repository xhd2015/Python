
from numpy import exp, linspace, meshgrid

from chaco.api import ArrayPlotData, Plot, jet
from enable.component_editor import ComponentEditor
from traits.api import HasTraits, Instance
from traitsui.api import Item, View


class ImagePlot(HasTraits):

    plot = Instance(Plot)

    traits_view = View(Item('plot', editor=ComponentEditor(),
                            show_label=False),
                       width=500, height=500,
                       resizable=True,
                       title="Chaco Plot")

    def _plot_default(self):
        # Create the data and the PlotData object.  For a 2D plot, we need to
        # create a grid of X and Y points using meshgrid.
        x = linspace(0, 10, 51)
        y = linspace(0, 5, 51)
        X, Y = meshgrid(x, y)
        z = exp(-(X**2 + Y**2) / 100)
        plotdata = ArrayPlotData(zdata=z[:-1, :-1])
        # Create a Plot and associate it with the PlotData.
        plot = Plot(plotdata)
        # Create a line plot in the Plot
        plot.img_plot("zdata", xbounds=x, ybounds=y, colormap=jet)
        return plot


demo = ImagePlot()
if __name__ == "__main__":
    demo.configure_traits()
