#############################################################################
# school_class_1.py
#
# 1. List Trait
# 2. Static List Observer functions (_xyz_changed and _xyz_items_changed)
#############################################################################

# enthought imports
from traits.api import HasTraits, Str, List
from traitsui.api import View, Item, Group, ListEditor

class SchoolClass(HasTraits):
    """ Tracks the personnel in a classroom.
    """
    
    # name of the class teacher
    teacher = Str

    # List of the students in the class
    students = List(Str)
    
    view = View('teacher',
                Group(
                      Item('students', 
                           style='custom',
                           editor=ListEditor(rows=5),
                           show_label=False,
                      ),
                      show_border=True,
                      label='Students'
                ),      
                title = 'Class',
                width=300,
                height=200,
                resizable=True
            )
                
    #########################################################################
    # Protected interface
    #########################################################################    

    # static trait observers ################################################

    def _students_changed(self, old, new):
        print "The entire class has changed:", new
    
    def _students_items_changed(self, event):
        """ Handle the case when items within the list are changed.
        
            event.added -- A list of the items added to students
            event.removed -- A list of the items removed from students
            event.index -- The start index of the items that were added
                           or removed.
        """
        if event.added:
            print "students added (index,name):", event.index, event.added
        if event.removed:
            print "students removed (index,name):", event.index, event.removed

#############################################################################
# Demo Code
#############################################################################

school_class = SchoolClass()
school_class.teacher = "Molly"

# set up the initial set of students.
school_class.students = ["John", "Jane", "Jill"]

# add a student
school_class.students.append("Bill")

# add several students
school_class.students.extend(["Sue", "Betty"])

# remove some students
del school_class.students[1:3]
