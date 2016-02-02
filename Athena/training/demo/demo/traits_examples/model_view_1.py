from traits.api import HasTraits, Range, Property, Instance, \
                                 Float, Delegate
from traitsui.api import View, Item

class Reactor(HasTraits):
    core_temperature = Range(-273.0, 100000.0)
      
class ReactorModelView(HasTraits):

    model = Instance(Reactor)
    
    # The "dummy" view of the reactor should be a warning string.
    core_temperature = Property(depends_on='model.core_temperature')
        
    def _get_core_temperature(self):
        temp = self.model.core_temperature
        if temp <= 500.0:
           return 'Normal'
        if temp < 2000.0:
           return 'Warning'
        return 'Meltdown'

my_view = View(Item('core_temperature', style = 'readonly'))

# Demo Code
reactor = Reactor( core_temperature = 200.0 )
view = ReactorModelView(model=reactor)
view.edit_traits(view=my_view)

# Now change the temperature
reactor.core_temperature = 5000.0
