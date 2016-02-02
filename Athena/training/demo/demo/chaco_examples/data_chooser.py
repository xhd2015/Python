
from numpy import linspace
from scipy.special import jn

from chaco.api import ArrayPlotData, Plot
from enable.component_editor import ComponentEditor
from traits.api import Dict, Enum, HasTraits, Instance
from traitsui.api import Item, View


class DataChooser(HasTraits):

    plot = Instance(Plot)

    data_name = Enum("jn0", "jn1", "jn2")

    data = Dict

    traits_view = View(Item('data_name', label="Y data"),
                       Item('plot', editor=ComponentEditor(),
                            show_label=False),
                       width=800, height=600, resizable=True,
                       title="Data Chooser")

    def _plot_default(self):
        x = linspace(-5, 10, 100)
        self.data = dict(jn0=jn(0, x), jn1=jn(1, x), jn2=jn(2, x))
        # Create the data and the PlotData object
        plotdata = ArrayPlotData(x=x, y=self.data[self.data_name])

        # Create a Plot and associate it with the PlotData
        plot = Plot(plotdata)

        # Create a line plot in the Plot
        plot.plot(("x", "y"), type="line", color="blue")

        return plot

    def _data_name_changed(self, old, new):
        self.plot.data.set_data("y", self.data[self.data_name])


demo = DataChooser()
if __name__ == "__main__":
    demo.configure_traits()
