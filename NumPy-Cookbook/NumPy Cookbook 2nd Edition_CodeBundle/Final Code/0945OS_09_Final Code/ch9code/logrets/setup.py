from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("log_returns", ["logrets.pyx"])]

setup(
        name = 'Log returns app',
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext_modules
     )
