# Use the load function to read a Python dictionary from a pickle file.
# First run demo1_save.py to create the pickle file 'demo1.pkl'.

from cPickle import load

with open('demo1.pkl', 'rb') as f:
    data = load(f)

print "data =", data
