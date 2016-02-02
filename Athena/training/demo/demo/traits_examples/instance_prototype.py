from traits.api import HasTraits, Instance, Str, PrototypedFrom

class Person(HasTraits):

    first_name = Str("John")
    last_name = Str("Doe")

    def __repr__(self):
        return 'Person("%s %s")' % (self.first_name, self.last_name)

class Child(Person):

    parent = Instance(Person, args=())
    last_name = PrototypedFrom('parent', 'last_name')

    def _last_name_changed(self, old, new):
        print "child's last name changed:", new

# Demo Code
dad = Person(first_name="Sam", last_name="Barns")
child = Child(first_name="Jane", parent=dad)
print "Dad:", dad
print "Child:", child
child.last_name = "Smith"
print "Dad:", dad
print "Child:", child

