from traits.api import HasTraits, Range, Instance, Property
from traitsui.api import View, Item, ModelView

class Reactor(HasTraits):

   core_temperature = Range(-273.0, 100000.0)

   water_level = Float

class ReactorModelView(ModelView):

    core_temperature = Property(depends_on='model.core_temperature')

    _ = Delegate(model, '*') 
    
    def _get_core_temperature(self):
        temp = self.model.core_temperature
        if temp <= 500.0:
           return 'Normal'
        if temp < 2000.0:
           return 'Warning'
        return 'Meltdown'

my_view = View(
               Item('core_temperature', style = 'readonly'),
               Item('water_level'),
          )

reactor = Reactor( core_temperature = 200.0 )
view = ReactorModelView(model=reactor)
view.edit_traits(view=my_view)
