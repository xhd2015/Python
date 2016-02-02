
import numpy as np

from traits.api import HasTraits, Array
from traitsui.api import View, Item, ArrayEditor


class Data(HasTraits):

    a = Array()

    def _a_default(self):
        a = np.array([[1.0, 2.0], [3.0, 4.0]])
        return a

    traits_view = View(Item('a', editor=ArrayEditor()),
                       Item('a', editor=ArrayEditor(), style='readonly'),
                       Item('a', editor=ArrayEditor(width=48)))


if __name__ == "__main__":
    data = Data()
    data.configure_traits()
