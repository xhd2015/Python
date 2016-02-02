#############################################################################
# table_2.py
#
# 1. Define a TableEditor.
# 2. Define a set of table column formats and order them within the table.
# 3. Get rid of the buttons and filters at the top.
# 4. Set the size of the view.
#############################################################################

# enthought imports
from traitsui.api import View, Item, Group, TableEditor
from traitsui.table_column import ObjectColumn

from traits.api import HasTraits, Str, Int, Enum, List, Bool, Regex

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

employees_editor = TableEditor(columns = [ObjectColumn(name = 'retired',
                                                       label = 'Retired'),
                                          ObjectColumn(name = 'first_name',
                                                       label = 'First'),
                                          ObjectColumn(name = 'last_name',
                                                       label = 'Last'),
                                          ObjectColumn(name = 'gender',
                                                       label = 'Gender'),                             
                                         ],
                               configurable=False, # removes table buttons
                               sortable=False,     # removes buttons
                               )
    
view = View(
            Group(
                  Item('employees', show_label=False,
                       editor=employees_editor
                      ),
                  show_border=True,
                  label="Employees",    
                 ),
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
