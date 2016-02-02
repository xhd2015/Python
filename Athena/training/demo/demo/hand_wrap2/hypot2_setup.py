from distutils.core import Extension, setup

ext = Extension(name="hypot2",
                sources=['hypot.c', 'hypot2_module.c'],
                include_dirs=['.'])

if __name__ == '__main__':
    setup(name='foo',
          version='1.0',
          ext_modules=[ext])                