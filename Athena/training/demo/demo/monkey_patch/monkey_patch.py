class Foo(object):
    
    def out(self):
        print 'You are here'
        

def out2(self):
    print 'Not any more!!'


foo = Foo()
foo.out()

Foo.out = out2
foo.out()    