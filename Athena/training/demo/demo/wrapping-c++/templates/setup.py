from numpy.distutils.core import setup, Extension

sources = ['tmpl_list.i', 'tmpl_list.cxx']

setup(name = "_wrap", version = "1.0",
      ext_modules = [Extension("_tmpl_list", sources, swig_opts=['-c++'])])
