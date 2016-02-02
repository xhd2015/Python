
from traits.api import HasTraits, File
from traitsui.api import View


class CharacterCount(HasTraits):

    filename = File()

    traits_view = View('filename', width=400)

    def _filename_changed(self):
        fname = self.filename
        try:
            with open(fname, 'rb') as f:
                n = len(f.read())
            print '"{:s}" has {:d} chars.'.format(fname, n)
        except IOError:
            # Ignore file errors.
            pass


if __name__ == "__main__":
    cc = CharacterCount()
    cc.edit_traits()
