from traits.api import HasTraits, Float, Str

class Foo(HasTraits):
    bar = Float
    baz = Str
     
    def _anytrait_changed(self, name, old, new):
        print name, 'changed from', old, 'to', new
        
foo = Foo()
foo.bar = 10        
foo.baz = "hello"