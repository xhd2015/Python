from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext

import numpy

ext = Extension("pyx_lap", ["pyx_lap.pyx"],
                include_dirs = [numpy.get_include()])
setup(
  name = "PyrexGuide",
  ext_modules=[ext],
  cmdclass = {'build_ext': build_ext}
)

