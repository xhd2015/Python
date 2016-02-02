
from numpy import *
from numpy.lib.stride_tricks import as_strided

# 2 seconds at 1 KHz sample rate.
t = arange(0, 2.0, 0.001)
# Create three sine waves, with
# frequencies in w.
w = array([1,3,7]).reshape(-1,1)
sig = sin(2*pi*w*t)
# Compute averages over 125 samples
# (125 milliseconds), every 25 samples.
c = 125
k = 25
r = (sig.shape[1] - c + k) / k
nb = sig.itemsize
strides = (sig.strides[0], k*nb, nb)
view = as_strided(sig, shape=(3, r, c),
                    strides=strides)
avg = view.mean(axis=-1)
# Create a matching t array.
tview = as_strided(t, shape=(r,c), strides=(k*nb,nb))
tavg = tview.mean(axis=-1)

# plot(tavg, avg)
