
from numpy import linspace, sin

from enable.api import ColorTrait
from chaco.api import ArrayPlotData, Plot, marker_trait
from enable.component_editor import ComponentEditor
from traits.api import HasTraits, Instance, Int, Property
from traitsui.api import VGroup, Item, View, RangeEditor


class ScatterPlotTraits(HasTraits):

    plot = Instance(Plot)
    color = ColorTrait("blue")
    marker = marker_trait
    marker_size = Int(4)
    renderer = Property(depends_on=['plot'])

    traits_view = \
        View(
            VGroup(
                Item('color', label="Color", style="custom"),
                Item('marker', label="Marker"),
                Item('marker_size', label="Size",
                     editor=RangeEditor(low=1, high=20)),
                Item('plot', editor=ComponentEditor(), show_label=False),
            ),
            width=800, height=600, resizable=True,
            title="Chaco Plot"
        )

    def _plot_default(self):
        # Create the data and the PlotData object
        x = linspace(-14, 14, 100)
        y = sin(x) * x ** 3
        plotdata = ArrayPlotData(x=x, y=y)
        # Create a Plot and associate it with the PlotData
        plot = Plot(plotdata)
        # Create a line plot in the Plot.  Give it a name for easy access.
        plot.plot(("x", "y"), type="scatter", color="blue", name="XY")
        return plot

    def _get_renderer(self):
        return self.plot.plots['XY'][0]

    def _color_changed(self):
        self.renderer.color = self.color

    def _marker_changed(self):
        self.renderer.marker = self.marker

    def _marker_size_changed(self):
        self.renderer.marker_size = self.marker_size


demo = ScatterPlotTraits()

if __name__ == "__main__":
    demo.configure_traits()
