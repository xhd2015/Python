# Standard library imports
import os
import gzip
from uuid import uuid4
from urllib import urlretrieve

# Numeric library imports
from scipy import io

# Plotting imports
from pylab import imshow, show

url = "ftp://math.nist.gov/pub/MatrixMarket2/SPARSKIT/fidap/fidap005.mtx.gz"
fname = uuid4().get_hex() + ".mtx.gz"
print "Downloading Matrix Market; this may take a minute..."
urlretrieve(url, fname)

# Open the compressed file using the gzip library.
compressed_file = gzip.open(fname)

# Use the matrix-market reader from scipy to load the matrix into
# a sparse matrix.
sparse_a = io.mmread(compressed_file)

# Convert from sparse to dense array format.
dense_a = sparse_a.toarray()

# Display the downloaded matrix.
imshow(dense_a)
show()

# Cleanup.  Delete the downloaded file.
compressed_file.close()
os.remove(fname)
