from math import pi

from traits.api import HasTraits, Instance, DelegatesTo
from traitsui.api import View, Item, RangeEditor, UItem, Group
from enable.api import ComponentEditor
from chaco.api import Plot, ArrayPlotData

# Local import
from damped_osc import DampedOsc


class DampedOscView(HasTraits):
    """
    Access the model traits using DelegatesTo().
    """

    model = Instance(DampedOsc)

    x = DelegatesTo('model')
    y = DelegatesTo('model')
    a = DelegatesTo('model')
    b = DelegatesTo('model')
    omega = DelegatesTo('model')
    phase = DelegatesTo('model')

    plot = Instance(Plot)

    traits_view = \
        View(
            Group(
                UItem('plot', editor=ComponentEditor(), style='custom'),
            ),
            Item('a', label='a', editor=RangeEditor(low=0.0, high=10.0)),
            Item('b', label='b', editor=RangeEditor(low=0.0, high=2.0)),
            Item('omega', label='omega',
                 editor=RangeEditor(low=0.0, high=10.0)),
            Item('phase', label='phase',
                 editor=RangeEditor(low=-pi, high=pi,
                                    low_label='-pi', high_label="pi")),
            resizable=True,
            width=600,
            height=550,
            title="a * exp(-b*x) * cos(omega*x + phase)",
        )

    def _plot_default(self):
        data = ArrayPlotData(x=self.x, y=self.y)
        plot = Plot(data)
        plot.plot(('x', 'y'), style='line', color='green')
        plot.value_range.set_bounds(-self.a, self.a)
        return plot

    def _y_changed(self):
        # Get the plot's ArrayPlotData object.
        data = self.plot.data
        # Update the value of y in the ArrayPlotData.
        data.set_data('y', self.y)

    def _a_changed(self):
        self.plot.value_range.set_bounds(-self.a, self.a)


if __name__ == "__main__":
    osc = DampedOsc()
    osc_viewer = DampedOscView(model=osc)
    # We use edit_traits(), so this script should be run from within ipython.
    osc_viewer.edit_traits()
