from traits.api import (HasTraits, Instance, Array, on_trait_change, Int, DelegatesTo)
from traitsui.api import (View, Item, UItem, Group)
from enable.api import ComponentEditor
from chaco.api import Plot, ArrayPlotData, jet, VPlotContainer

import numpy as np

class Model(HasTraits):

    x_range = Array()
    y_range = Array()
    z_data = Array()

    cut_index = Int()

    def _cut_index_changed(self):
        if self.cut_index < 0:
            self.cut_index = 0
        if self.cut_index >= self.z_data.shape[0]:
            self.cut_index = self.z_data.shape[0] - 1

    def _x_range_default(self):
        return np.linspace(0, 10, 51)

    def _y_range_default(self):
        return np.linspace(0, 5, 51)

    def _z_data_default(self):
        self.compute_z_data()
        return self.z_data

    @on_trait_change('x_range, y_range')
    def compute_z_data(self):
        X, Y = np.meshgrid(self.x_range, self.y_range)
        self.z_data = np.exp(-(X**2 + Y**2) / 100)


# The view for the plots
class PlotsUI(HasTraits):

    composite_plot = Instance(VPlotContainer)
    line_plot = Instance(Plot)
    img_plot = Instance(Plot)

    plotdata = Instance(ArrayPlotData)

    traits_view = View(
            Group(
                Item('composite_plot',
                    editor=ComponentEditor(),
                    show_label=False),
                orientation = "vertical"),
            resizable=True, title="Two Chaco Plots"
            )

    def _plotdata_default(self):
        empty = np.array([])
        return ArrayPlotData(x=empty,
                             y=empty,
                             x_range=empty,
                             y_range=empty,
                             z_data=empty)


    def _composite_plot_default(self):

        line_plot = Plot(self.plotdata)
        line_plot.plot(('x', 'y'), type='line', color='blue')

        img_plot = Plot(self.plotdata)
        img_plot.img_plot("zdata",
                          xbounds='x_range',
                          ybounds='y_range',
                          colormap=jet)

        cp = VPlotContainer()
        cp.add(img_plot)
        cp.add(line_plot)
        return cp

    def update(self, model):
        self.plotdata.set_data('x', np.arange(model.z_data.shape[0]))
        self.plotdata.set_data('y', model.z_data[:, model.cut_index])
        self.plotdata.set_data('zdata', model.z_data[:-1, :-1])
        self.plotdata.set_data('x_range', model.x_range)
        self.plotdata.set_data('y_range', model.y_range)
        self.composite_plot.invalidate_draw()
        self.composite_plot.request_redraw()


# Pull together the model and view inside the Controller
class Controller(HasTraits):

    model = Instance(Model)
    view = Instance(PlotsUI)

    cut_index = DelegatesTo('model')

    traits_view = View(
            Group(
                UItem('@view'),
                Item('cut_index'),
                )
            )

    @on_trait_change('model, view')
    def update_view(self):
        print "update_view, cutplane", self.cut_index
        if self.model is not None and self.view is not None:
            self.view.update(self.model)

    def _cut_index_changed(self):
        self.view.update(self.model)

    def _model_changed(self):
        if self.view is not None:
            self.view.update(self.model)


if __name__ == '__main__':
    Controller(model=Model(), view=PlotsUI()).configure_traits()
