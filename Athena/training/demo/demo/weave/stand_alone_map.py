import string
from scipy.weave import ext_tools


def build_ex1():
    ext = ext_tools.ext_module('_ex1')
    # Type declarations - define a sequence and a function
    seq = []
    func = string.upper
    code = """
           py::tuple args(1);
           py::list result(seq.length());
           for(int i = 0; i < seq.length();i++)
           {
              args[0] = seq[i];
              result[i] = func.call(args);
           }           
           return_val = result;
           """
    func = ext_tools.ext_function('my_map', code, ['func', 'seq'])
    ext.add_function(func)
    ext.compile()


try:
    from _ex1 import *
except ImportError:
    build_ex1()
    from _ex1 import *

if __name__ == '__main__':
    print my_map(string.lower, ['asdf', 'ADFS', 'ADSD'])
