from traits.api import HasTraits, List, Str, Int, Instance

class Person(HasTraits):
    name = Str
    age = Int
        
class SchoolClass(HasTraits):
    teacher = Instance(Person)
    students = List(Person)

    def _anytrait_changed_for_teacher(self, object, name, old, new):
        print 'any:', name, new
        
    def _age_changed_for_teacher(self, object, name, old, new):
        print 'The teacher is now', new, 'years old.'

    def _age_changed_for_students(self, object, name, old, new):
        print object.name, 'is now', new, 'years old.'

# Demo Code
the_class = SchoolClass()

teacher_ben = Person(name="Ben", age=35)
the_class.teacher = teacher_ben

bob = Person(name="Bob", age=10)
the_class.students.append(bob)

jane = Person(name="Jane", age=11)
the_class.students.append(jane)

# This will call the observer in SchoolClass
teacher_ben.age = 36

new_teacher = Person(name="Foo", age=30)
the_class.teacher = new_teacher
print new_teacher

# As will fire the observer in SchoolClass
bob.age = 11

# Remove Bob from the Class and the observer is no longer called.
the_class.students.remove(bob)
bob.age = 12
