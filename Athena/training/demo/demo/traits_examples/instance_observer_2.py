from traits.api import HasTraits, List, Str, Int, Instance, on_trait_change

class Person(HasTraits):
    name = Str
    age = Int
        
class SchoolClass(HasTraits):
    teacher = Instance(Person)
    students = List(Person)
      
    @on_trait_change('teacher.age')
    def _teacher_update(self, object, name, old, new):
        if name == 'teacher':
            print 'The teacher is now', new.age, 'years old.'
        elif name == 'age':    
            print 'The teacher is now', new, 'years old.'

    @on_trait_change('students.age')
    def _student_update(self, object, name, old, new):
        print object.name, 'is now', new, 'years old.'

# Demo Code
teacher_ben = Person(name="Ben", age=35)
the_class = SchoolClass(teacher=teacher_ben)

bob = Person(name="Bob", age=10)
the_class.students.append(bob)

jane = Person(name="Jane", age=11)
the_class.students.append(jane)

# This will call the observer in SchoolClass
teacher_ben.age = 36

# As will fire the observer in SchoolClass
bob.age = 11

# Remove Bob from the Class and the observer is no longer called.
the_class.students.remove(bob)
bob.age = 12
