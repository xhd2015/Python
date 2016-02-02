from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  ext_modules=[ Extension("inc", ["inc.pyx"]) ],
  cmdclass = {'build_ext': build_ext}
)

