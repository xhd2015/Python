"""Interactive degree 2 polynomial plotter."""

from traits.api import (HasTraits, Float, Array, Property,
        Instance, on_trait_change)
from traitsui.api import View, Item, RangeEditor
from enable.component_editor import ComponentEditor
from chaco.api import ArrayPlotData, Plot

from numpy import linspace


class Poly(HasTraits):

    a = Float(2.0)
    b = Float(3.0)
    c = Float(4.0)

    x = Array

    y = Property(depends_on=['a', 'b', 'c', 'x'])

    plot = Instance(Plot)
    plotdata = Instance(ArrayPlotData)

    view = View(
            Item('plot', editor=ComponentEditor(), show_label=False),
            Item('a', editor=RangeEditor(low=-5., high=5.)),
            Item('b', editor=RangeEditor(low=-5., high=5.)),
            Item('c', editor=RangeEditor(low=-5., high=5.)),
            height=500,
            width=600,
            resizable=True,
            title="Poly Plot")

    def _get_y(self):
        return self.a * self.x ** 2 + self.b * self.x + self.c

    def _x_default(self):
        return linspace(0, 10, 101)

    def _plotdata_default(self):
        data = ArrayPlotData(x=self.x, y=self.y)
        return data

    def _plot_default(self):
        plot = Plot(self.plotdata)
        plot.plot(("x", "y"), color="green")
        plot.title = "A*x**2 + B*x + C"
        plot.x_axis.title = "x"
        plot.y_axis.title = "y"
        return plot

    @on_trait_change('a, b, c')
    def update_y(self):
        self.plotdata.set_data('y', self.y)


poly = Poly()
#poly.edit_traits()
poly.configure_traits()
