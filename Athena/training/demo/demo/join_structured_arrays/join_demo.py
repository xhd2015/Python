
from numpy import genfromtxt
from numpy.lib import recfunctions


data1 = genfromtxt('data1.csv', names=True, delimiter=',', dtype=None)
data2 = genfromtxt('data2.csv', names=True, delimiter=',', dtype=None)

combined = recfunctions.join_by('Name', data1, data2, jointype='outer')

fields = combined.dtype.names
for name in fields:
    print "%-10s" % name,
print
for row in combined:
    for name in fields:
        print "%-10s" % row[name],
    print



# Notes:
# 1. `combined` is a masked array.
# 2. join_by() will break if the maximum length of the data in the 'Name'
#    field is not the same in the two data files.
