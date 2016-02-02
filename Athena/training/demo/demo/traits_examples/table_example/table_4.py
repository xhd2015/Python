#############################################################################
# table_4.py
#
# 1. Add ability to create/delete employees through the table.
#############################################################################

# enthought imports
from traitsui.api import View, Item, Group, TableEditor
from traitsui.table_column import ObjectColumn
from traitsui.menu import OKButton, CancelButton, HelpButton

from traits.api import HasTraits, Str, Int, Enum, List, Bool, Regex

# Local imports
from square_checkbox_column import SquareCheckboxColumn

ssn_trait = Regex('000-00-0000',regex = '\d\d\d[-]\d\d[-]\d\d\d\d')

class Employee(HasTraits):
    
    first_name = Str(desc='First name of the Employee')
    last_name = Str
    gender = Enum('male', 'female')
    ssn = ssn_trait
    retired = Bool
    
class Company(HasTraits):
    
    employees = List(Employee)

############################################################################
# Views and Editors
############################################################################

employees_editor = TableEditor(columns = [SquareCheckboxColumn(name='retired',
                                                               label='Retired',
                                                               width=50),
                                          ObjectColumn(name = 'first_name',
                                                       label = 'First',
                                                       width=0.35),
                                          ObjectColumn(name = 'last_name',
                                                       label = 'Last',
                                                       width=0.35),
                                          ObjectColumn(name = 'gender',
                                                       label = 'Gender',
                                                       width=0.20),                             
                                         ],
                               configurable=False, # removes table buttons
                               sortable=False,     # removes buttons
                               # These lines allow you to add new employees
                               row_factory = Employee,
                               deletable=True,

                               # This allows you to add automatically without
                               # a button.
                               #auto_add=True,
                               )
    
view = View(
            Group(
                  Item('employees', show_label=False,
                       editor=employees_editor
                      ),
                  show_border=True,
                  label="Employees",    
                 ),
            buttons=[OKButton, CancelButton],
            resizable=True,
            width=400,
            height=600,
           )
                
#############################################################################
# Demo Code
#############################################################################

company = Company()
company.employees.append(Employee(first_name="Bob", last_name="Doe",
                                  gender="male"))
company.employees.append(Employee(first_name="John", last_name="Smith",
                                  gender="male"))
company.employees.append(Employee(first_name="Sally", last_name="Jones",
                                  gender="female"))

company.edit_traits(view=view)    
