from traits.api import HasTraits, Property, TraitError, Int

def validate_odd(object, name, value):
    """ Property Validator to check for odd values
    """
    print 'validate:', object, name, value
    if value % 2 == 0:
        raise TraitError, "You gave me an even number."
        
    return value
    
def validate_even(object, value):
    """ Property Validator to check for even values
        The signature is different from the validate_odd example
        for demo purposes.
    """
    print 'validate:', object, value

    if value % 2 == 1:
        raise TraitError, "You gave me an odd number."
        
    return value
    
class Foo(HasTraits):

    # Two traits properties with special validation
    odd_value = Property(fvalidate=validate_odd)    
    even_value = Property(fvalidate=validate_even)    

    # shadow variables for the even and odd properties
    _odd_value = Int    
    _even_value = Int
    
    def _get_odd_value(self):
        return self._odd_value
    
    def _set_odd_value(self, value):
        self._odd_value = value

    def _get_even_value(self):
        return self._even_value
    
    def _set_even_value(self, value):
        self._even_value = value


# Demo Code        
foo = Foo()

foo.odd_value = 3
print foo.odd_value

foo.even_value = 2
print foo.even_value

# THESE SHOULD BOTH THROW EXCEPTIONS
try:
    foo.odd_value = 4
except TraitError:
    print "good: 4 isn't odd"    

try:
    foo.even_value = 5
except TraitError:
    print "good: 5 isn't even"    
    
