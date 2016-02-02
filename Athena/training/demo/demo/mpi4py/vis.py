#!/usr/bin/env python

import numpy as np
import pylab as pl
import sys

try:
    a = np.load(sys.argv[1])
except IOError:
    a = np.fromfile(sys.argv[1], dtype=np.float64)
    a.shape = (int(np.sqrt(a.size)), -1)

pl.imshow(a, interpolation='nearest', origin='lower')

pl.show()
