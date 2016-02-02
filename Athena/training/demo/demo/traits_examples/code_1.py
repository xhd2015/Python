from traits.api import HasTraits, File, Code
from traitsui.api import View

class Foo(HasTraits):
    file = File
    code = Code

    view = View('file', 'code',
                width=500,
                height=400,
                resizable=True)
                
    def _file_changed(self):
        print self.file
        self.code=open(self.file,'r').read()

foo = Foo()
foo.edit_traits()        
        
        