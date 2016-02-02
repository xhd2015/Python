def outer():
    a = 1
    def inner():
        print a
    inner()

# This will print 1
outer()

# function closure
def outer():
    a = 1 
    def inner():
        return a
    return inner
    
func = outer()

print 'func returns a (1):', func()    