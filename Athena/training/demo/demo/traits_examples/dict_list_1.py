from traits.api import HasTraits, Float, List, Dict, Str, Int

class Foo(HasTraits):
    a = List([1,2,3], Int, minlen=3)
    b = Dict(Str)
    
    # bar = Float
    # 
    # def _anytrait_changed(self, name, old, new):
    #    print name, 'changed from', old, 'to', new
        
#foo = Foo()
#foo.bar = 10        

foo = Foo()
print foo.a
foo2 = Foo()
foo2.a[1] = 10
print foo.a

#foo.b[1] = 'adsf' 