from traits.api import HasTraits, Tuple, Int, Str, Float

class Foo(HasTraits):
    
    # A tuple of any size and with any argument types
    a = Tuple
    
    # Tuple with 2 elements that have the types Int, Str respectively
    b = Tuple(Int, Str)
    
    # Tuple with 3 with types (Int, Str, Float) elements.
    # The first argument is the default value of the list.
    c = Tuple((2,"goodbye", 2.0), Int, Str, Float)
    
foo = Foo()

foo.a = (1,2,3,4)

print foo.c
foo.c = (1,"hello", 3.0)
print foo.c    

foo.b = (1,"bar")
