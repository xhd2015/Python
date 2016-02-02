def foo():
    print "hello"

def bar():
    print "goodbye"
    

foo()
foo.func_code = bar.func_code
foo()    