""" 
Trait Person
------------

Define a Traits based class for a Person.

Hint: See the demo/traits_examples/configure_ui_1.py 

1. Define a person class. A person should have a 
   :attr:`first_name` and :attr:`last_name` that are both strings, 
   an :attr:`age` that is a Float value, and a :attr:`gender` that is 
   either 'male' or 'female'.  After defining the class,
   create an instance of it and set/get some its traits
   to test its behavior.  Try setting names to strings
   and floats and see what happens.
   
2. Add a static trait listener that prints the age when 
   it changes.

3. Create a UI that groups the name at the top of a dialog
   with the gender and age below.
   
See :ref:`trait-person-solution`.
"""
from traitsui.api import View, VGroup, HGroup, Group, Item
from traits.api import HasTraits, Float, Str, Enum

class Person(HasTraits):
    # Put your code here.
    pass
            
person = Person()   
person.edit_traits()