from traits.api import HasTraits, Instance, Str

class Person(HasTraits):

    first_name = Str("John")
    last_name = Str("Doe")
    
    def __repr__(self):
        return 'Person("%s %s")' % (self.first_name, self.last_name)
        
class Family(HasTraits):

    # Instantiate the default Person
    dad = Instance(Person,args=())
    
    # Instantiate a Person object with a different first name
    mom = Instance(Person, args=(), kw={'first_name':'Jane'})
    
    # Son is a Person object, but it defaults to 'None'     
    son = Instance(Person)
    
    # In case you need "forward" declarations, you can use 
    # the name as a string.  Default is None
    daughter = Instance('Person')
    
# Demo Code    
family = Family()

print 'Dad:', family.dad    
print 'Mom:', family.mom

print 'son:', family.son
print 'daughter:', family.daughter

family.son = Person(first_name="Bubba")
family.daughter = Person(first_name='Sissy')

print 'son:', family.son
print 'daughter:', family.daughter