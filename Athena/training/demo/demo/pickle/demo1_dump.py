# Use the dump() function to pickle a dictionary to a file.

from cPickle import dump

data = {'foo': [1, 2], (0,1): 1.5}

with open('demo1.pkl', 'wb') as f:
    dump(data, f)
