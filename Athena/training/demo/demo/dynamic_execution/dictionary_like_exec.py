class LoudDict(dict):
    """ This dictionary announces whenever one of its values
        is get or set.
    """
    def __getitem__(self, key):
        value = super(LoudDict, self).__getitem__(key)
        print "retrieving %s which is %s" % (key, value)
        
        return value

    def __setitem__(self, key, value):
        print "setting %s = %s" % (key, value)
        super(LoudDict, self).__setitem__(key, value)

local = LoudDict(a=1)
exec "b=a+1" in {}, local
print local