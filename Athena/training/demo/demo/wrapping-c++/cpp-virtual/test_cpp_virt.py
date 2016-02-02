import cpp_virt

class PythonDerived(cpp_virt.base):

    def __init__(self):
        super(PythonDerived, self).__init__()

    def frobnicate(self, i):
        print "frobnicate from PythonDerived"
        return i**2


pd = PythonDerived()
assert pd.call_frob(100) == 100**2
