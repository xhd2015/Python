from numpy.distutils.core import setup, Extension
import os
       
os.system("swig -python example.i")
       
sources = ['example_wrap.c','fact.c']

setup(name = "_example", version = "1.0",
      ext_modules = [Extension("_example", sources)])
