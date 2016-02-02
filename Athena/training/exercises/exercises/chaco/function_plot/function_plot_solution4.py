from math import pi

from traits.api import Instance, on_trait_change
from traitsui.api import ModelView, View, Group, Item, UItem, RangeEditor
from enable.api import ComponentEditor
from chaco.api import Plot, ArrayPlotData

from damped_osc import DampedOsc


class DampedOscView4(ModelView):
    """
    In the View, access the model traits as model.a, etc.

    Outside the View, access model traits as model.a, etc.
    """
    model = Instance(DampedOsc)

    plot = Instance(Plot)

    traits_view = \
        View(
            Group(
                UItem('plot', editor=ComponentEditor(), style='custom'),
            ),
            Item('model.a', label='a', editor=RangeEditor(low=0.0, high=10.0)),
            Item('model.b', label='b', editor=RangeEditor(low=0.0, high=2.0)),
            Item('model.omega', label='omega',
                 editor=RangeEditor(low=0.0, high=10.0)),
            Item('model.phase', label='phase',
                 editor=RangeEditor(low=-pi, high=pi,
                                    low_label='-pi', high_label="pi")),
            title="Function Plotter",
            resizable=True,
            width=600,
            height=550,
        )

    def _plot_default(self):
        data = ArrayPlotData(x=self.model.x, y=self.model.y)
        plot = Plot(data)
        plot.plot(('x', 'y'), style='line', color='green')
        plot.value_range.set_bounds(-self.model.a, self.model.a)
        plot.title = "a * exp(-b*x) * cos(omega*x + phase)"
        return plot

    @on_trait_change('model.y')
    def y_updated(self):
        # Get the plot's ArrayPlotData object.
        data = self.plot.data
        data.set_data('y', self.model.y)

    @on_trait_change('model.a')
    def a_updated(self):
        self.plot.value_range.set_bounds(-self.model.a, self.model.a)


if __name__ == "__main__":
    func = DampedOsc()
    func_viewer = DampedOscView4(model=func)
    func_viewer.edit_traits()
