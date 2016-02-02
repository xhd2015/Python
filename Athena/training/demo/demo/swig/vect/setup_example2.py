from numpy.distutils.core import setup, Extension
import os


os.system("swig -python example2.i")

sources = ['example2_wrap.c', 'vect.c']

setup(name="_example2",
      version="1.0",
      ext_modules=[Extension("_example2", sources)])
