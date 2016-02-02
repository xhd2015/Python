
from traits.api import HasTraits, Button, Bool
from traitsui.api import View, UItem, Group


class ButtonDemo(HasTraits):

    available = Bool(True)

    click = Button("Press Here")

    traits_view = View(Group('available'),
                       UItem('click', enabled_when='available'))

    def _click_fired(self):
        print "You clicked the button."


if __name__ == "__main__":
    b = ButtonDemo()
    b.configure_traits()
