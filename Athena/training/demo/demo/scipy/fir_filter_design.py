"""
FIR filter design example; requires SciPy 0.9 or later.
"""

import numpy as np
from scipy.signal import firwin2, freqz, kaiserord
from matplotlib.pylab import plot, show, grid, xlabel, ylabel, legend, title

# Bandpass with a notch.
desired_freq = [0.0, 0.1, 0.2, 0.56, 0.6,  0.64, 0.8, 0.9, 1.0]
desired_gain = [0.0, 0.0, 1.0, 1.0,  0.75, 1.0,  1.0, 0.0, 0.0]

# Use firwin2 with a Kaiser window to design the filter.
ntaps, beta = kaiserord(ripple=65, width=0.08)
taps = firwin2(ntaps, desired_freq, desired_gain, window=('kaiser', beta))

# Compute the filter's response.
w, h = freqz(taps, [1.0], worN=8000)

# Plot the desired and actual responses.
plot(desired_freq, desired_gain, 'g-', label='Desired')
plot(w/np.pi, np.abs(h), 'b', label='Computed')
xlabel('Frequency (rel. to Nyquist)')
ylabel('Gain')
title('FIR Filter Frequency Response (%d taps)' % ntaps)
legend()
grid(True)
show()
