from numpy.distutils.core import Extension

fcopy1 = Extension(name='fcopy',
                   sources=['fcopy.pyf','fcopy.f'])

fcopy2 = Extension(name='fcopy2',
                   sources=['fcopy2.pyf', 'fcopy.f'])

if __name__ == "__main__":
    from numpy.distutils.core import setup

    setup(name='fcopy',
          description = "f2py example",
          ext_modules = [fcopy1, fcopy2],
    )
