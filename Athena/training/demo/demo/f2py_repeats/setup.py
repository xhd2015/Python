from numpy.distutils.core import Extension

futil1 = Extension(name='futil',
                   sources=['futil.pyf','futil.f'])

futil2 = Extension(name='futil2',
                   sources=['futil2.f'])

if __name__ == "__main__":
    from numpy.distutils.core import setup

    setup(name='futil',
          description = "f2py example",
          ext_modules = [futil1, futil2],
          py_modules = ['util']
    )
# End of setup example.py