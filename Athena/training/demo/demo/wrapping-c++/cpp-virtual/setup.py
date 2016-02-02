from numpy.distutils.core import setup, Extension
import os

os.system("swig -c++ -python _cpp_virt.i")
       
sources = ['_cpp_virt_wrap.cxx','cpp_virt.cxx']

setup(name = "_cpp_virt", version = "1.0",
      ext_modules = [Extension("_cpp_virt", sources)])
