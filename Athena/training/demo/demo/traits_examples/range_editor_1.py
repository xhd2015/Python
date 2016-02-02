
from math import pi
from traits.api import HasTraits, Float
from traitsui.api import View, Item, RangeEditor


class Example(HasTraits):
    radius = Float
    angle = Float
    traits_view = View(
        Item('radius', editor=RangeEditor(low=0, high=10.0)),
        Item('angle', editor=RangeEditor(low=-pi, high=pi,
                                         low_label='-pi', high_label='pi')),
        title="RangeEditor Example")


if __name__ == "__main__":
    example = Example()
    example.edit_traits()

