from numpy.distutils.core import setup, Extension
import os


os.system("swig -python example3.i")

sources = ['example3_wrap.c', 'vect.c']

setup(name="_example3",
      version="1.0",
      ext_modules=[Extension("_example3", sources)])
