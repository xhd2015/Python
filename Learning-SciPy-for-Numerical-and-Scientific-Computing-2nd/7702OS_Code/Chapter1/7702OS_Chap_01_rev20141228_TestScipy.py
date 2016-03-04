'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2014 Sergio Rojas (srojas@usb.ve) 
and Erik A Christensen (erikcny@aol.com).

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

This code is used to display information about the packages
SciPy, Numpy, Matplotlib, IPython, and Pandas installed on 
a Python. It also performs the execution of tests suites included
with such packages.

Created on September, 21, 2014
Last Modified on: September, 21, 2014

'''

# Checking the Python Version installed on this system: 


import sys

import platform

print("\n")

print("Python distribution details: ")

print(sys.version)

print("\n")

print(str("Installed Python Version is: ")+str(platform.python_version()))



# Checking the Numpy Version installed on this system:

try:

  import numpy
  
  print(str("Installed Numpy version is: ")+str(numpy.__version__))

except ImportError:

  sys.exit("Error : Numpy can not be imported or is not installed.")



# Checking the Scipy Version installed on this system:

try:
  
  import scipy
  
  print(str("Installed Scipy version is: ")+str(scipy.__version__))

except ImportError:

  sys.exit("Error : Scipy can not be imported or is not installed.")



# Checking the Ipython Version installed on this system:
try:
  
  import IPython
  
  print(str("Installed IPython version is: ")+str(IPython.__version__))

except ImportError:

  sys.exit("Error : IPython can not be imported or is not installed.")



# Checking the Matplotlib Version installed on this system:
try:
  
  import matplotlib
  
  print(str("Installed Matplotlib version is: ")+str(matplotlib.__version__))

except ImportError:

  sys.exit("Error : Matplotlib can not be imported or is not installed.")



# Checking the Pandas Version installed on this system:
try:
  
  import pandas
  
  print(str("Installed Pandas version is: ")+str(pandas.__version__))

except ImportError:

  sys.exit("Error : Pandas can not be imported or not installed.")


print("\n")

print("\t    Necessary tools are installed. This system seems to be ready")

print("\t    to crunch numbers via python ...")


print("\n")

print("\t  There are some tests one can run to check...")

print("\t  if the installed packages work  correctly...")

print("\t  Each test takes some time. ...")



# This makes input to work in Python 2 and 3.

try: 
   
  input = raw_input

except NameError:
 
 pass


  print("\n")
print("\t  Would you like to run the NUMPY basic test suite...")

ans = input("For yes, enter y and hit return: ")

if ans=='y':

  print(str("Running some Numpy tests: "))

  numpy.test()


print("\n")

print("\t  Would you like to run the SCIPY basic test suite...")

ans = input("For yes, enter y and hit return: ")

if ans=='y':

  print(str("Running some Scipy tests: "))

  scipy.test()


print("\n")

print("\t  Would you like to run the MATPLOTLIB basic test suite...")

ans = input("For yes, enter y and hit return: ")

if ans=='y':

  print(str("Running some Matplotlib tests: "))

  matplotlib.test()


print("\n")

print("\t  Would you like to run the IPYTHON basic test suite...")

ans = input("For yes, enter y and hit return: ")

if ans=='y':

  print(str("Running some Ipython tests: "))

  IPython.test()
