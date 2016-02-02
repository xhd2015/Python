"""
Short-time Fourier Transform
----------------------------

The short-time Fourier transform is implemented by multiplying a segment of the
data by some kind of window function (boxcar, triangular, hamming, hanning,
blackman, etc.) and then taking the Fourier transform. This process is repeated
on a shifted segment of the data until all the data has been processed.

Exercise:

1.  The `read` function in scipy.io.wavfile can read in a .wav file. It takes the
    filename as input and returns the sample rate (in samples/sec) and 
    waveform data as output. [This has been done for you.]
2.  Perform the short-time Fourier transform on every 50 ms of data.
3.  Create an image showing the frequency on the horizontal axis and the
    center-point window time on the vertical axis. 
4.  (Bonus):  Label the axes with correct units and labels.

Note: If you would like to hear the sound, and have pyaudio installed,
run the play_audio.py file in this directory.
      
See: :ref:`short-time-fft-solution`.
"""

# Possibly useful functions
from scipy.io.wavfile import read
from scipy.fftpack import fft, fftfreq, fftshift
from scipy.signal import get_window  # useful for creating a window
from matplotlib.pyplot import figure, imshow, clf, gray, xlabel, ylabel

# Read in a wav file 
#   returns sample rate (samples / sec) and data
rate, data = read('scale.wav')



