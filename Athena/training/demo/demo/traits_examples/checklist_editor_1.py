
from traits.api import HasTraits, List, Str
from traitsui.api import View, Item, CheckListEditor

class Example(HasTraits):

    selection = List(Str)

    traits_view = View(
        Item('selection', style='custom',
            editor=CheckListEditor(
                            values=['egg', 'sausage', 'spam'])))

    def _selection_changed(self):
        print "selection is", self.selection


if __name__ == "__main__":
    example = Example()
    example.edit_traits()
