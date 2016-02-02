from math import pi

from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Group, Item, UItem, RangeEditor
from enable.api import ComponentEditor
from chaco.api import Plot, ArrayPlotData

# Local import
from damped_osc import DampedOsc


class DampedOscView2(HasTraits):
    """
    Use extended trait names in the View (e.g. 'object.model.a').

    Outside the View, access model traits as model.a, etc.
    """

    model = Instance(DampedOsc)

    plot = Instance(Plot)

    traits_view = \
        View(
            Group(
                UItem('plot', editor=ComponentEditor(), style='custom'),
            ),
            Item('object.model.a', label='a',
                 editor=RangeEditor(low=0.0, high=10.0)),
            Item('object.model.b', label='b',
                 editor=RangeEditor(low=0.0, high=2.0)),
            Item('object.model.omega', label='omega',
                 editor=RangeEditor(low=0.0, high=10.0)),
            Item('object.model.phase', label='phase',
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
    osc = DampedOsc()
    osc_viewer = DampedOscView2(model=osc)
    osc_viewer.edit_traits()
