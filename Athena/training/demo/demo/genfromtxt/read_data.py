"""A demonstration of numpy.genfromtxt."""
from numpy import genfromtxt

# Notes:
# * dtype=None tells genfromtxt to figure out the dtype from the file.
# * delimiter=',' tells genfromtxt that the field delimiter is a comma.
#   (The default is white space.)
# * names=True tells genfromtxt to use the column headings in the first line
#   as field names in a structured array.
# * A converter is used to convert the values in the second column to integer
#   code.  This allows the numpy array to be all integers.

material_codes = dict(oak=1, maple=2, birch=3, pine=4)

def convert(s):
    # Return 0 if s is not a known material.
    return material_codes.get(s, 0)


data = genfromtxt("data.csv", dtype=int, delimiter=',', names=True,
                  converters={1: convert})

print "data:"
print data
