from numpy.distutils.core import setup, Extension
import os
import numpy


os.system("swig -python rms.i")

ext = Extension("_rms",
                sources=['rms_wrap.c', 'rms.c'],
                include_dirs=[numpy.get_include()])

setup(name="_rms",
      version="0.0",
      ext_modules=[ext],
)
