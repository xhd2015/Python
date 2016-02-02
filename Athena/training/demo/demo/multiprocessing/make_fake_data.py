import numpy as np
import struct

def make_fake_data(fname, ncols, nrows):
    arr = np.random.randn(ncols, nrows)
    with open(fname, 'wb') as fh:
        fh.write(struct.pack('2I3s', nrows, ncols, arr.dtype.str))
        fh.write(arr.data)

if __name__ == '__main__':
    make_fake_data('fake_data.dat', ncols=10, nrows=1000)
