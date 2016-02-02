from numpy.distutils.core import setup, Extension

ext = Extension(name='nan2zero', sources=['nan2zero.c', 'nan2zero_wrap.c'])

setup(name="nan2zero", ext_modules=[ext])
