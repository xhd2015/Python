
from traits.api import HasTraits, Enum, Bool, List
from traitsui.api import View, Item, CheckListEditor


class Burger(HasTraits):

    # The number of patties.
    patties = Enum(1, 2)

    # Cheeseburger?
    cheese = Bool

    # List of condiments for the burger.
    condiments = List

    traits_view = \
        View(
            Item('patties', style='custom'),
            Item('cheese'),
            # Use the CheckListEditor instead of default.
            Item('condiments', style='custom',
                 editor=CheckListEditor(cols=3,
                            values=['ketchup', 'relish', 'mustard'])
            )
        )


if __name__ == "__main__":
    burger = Burger()
    burger.edit_traits()
