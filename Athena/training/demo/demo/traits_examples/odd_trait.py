from traits.api import HasTraits, BaseInt

class OddInt (BaseInt):

    # Define the default value:
    default_value = 1

    # Describe the trait type:
    info_text = 'an odd integer'

    def validate ( self, object, name, value ):
        value = super( OddInt, self ).validate( object, name, value )
        if (value % 2) == 1:
            return value

        self.error( object, name, value )


class Foo(HasTraits):
    value = OddInt
    

foo = Foo()

print 'odd default (1):', foo.value

foo.value = 3
print 'setting odd trait to 3:', foo.value

print 'attempt to set odd trait to even value'
print 'THIS WILL RAISE AN EXCEPTION'        
foo.value = 4