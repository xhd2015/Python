from numpy.distutils.core import setup, Extension
import os
import numpy


os.system("swig -python nan2zero.i")

ext = Extension("_nan2zero",
                sources=['nan2zero_wrap.c', 'nan2zero.c'],
                include_dirs=[numpy.get_include()])

setup(name="nan2zero",
      version="1.0",
      ext_modules=[ext],
)
