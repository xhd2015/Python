#############################################################################
# table_1.py
#
# !! Run outside of a shell -- this will hang IPython...
# 1. List of Instances displayed as a table by default.
#############################################################################

# enthought imports
from traitsui.api import View
from traits.api import HasTraits, Str, Regex, Int, Enum, List

ssn_trait = Regex('000-00-0000',regex = '\d\d\d[-]\d\d[-]\d\d\d\d')

class Employee(HasTraits):
    
    first_name = Str(desc='First name of the Employee')
    last_name = Str
    gender = Enum('male', 'female')
    ssn = ssn_trait

class Company(HasTraits):
    
    employees = List(Employee)
    
    view = View('employees',
                height=500,
                resizable=True)
                
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


company.edit_traits()    
