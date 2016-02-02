"""
A script to generate the simulated outputs of the
cocktail party microphones.
"""

import numpy as np
from scipy.io import wavfile


def get_wav(filename):
    freq, data = wavfile.read(filename)
    data = data.astype(float)
    if data.ndim > 1:
        # Flatten multiple channels.
        data = data.sum(axis=-1)
    return freq, data  


def double_rate(freq, data):
    freq2 = 2 * freq
    m = 0.5 * data[:-1] + 0.5 * data[1:]
    data2 = np.zeros(2 * data.size - 1)
    data2[::2] = data1
    data2[1:-1:2] = m
    return freq2, data2


if __name__ == "__main__":

    filename1 = 'wav/champion.wav'
    filename2 = 'wav/obiwan.wav'

    freq1, data1 = get_wav(filename1)
    freq2, data2 = get_wav(filename2)

    assert freq2 == 2*freq1

    freq1, data1 = double_rate(freq1, data1)

    # Normalize
    source1 = (data1 - data1.mean()) / data1.std()
    source2 = (data2 - data2.mean()) / data2.std()

    n = min(source1.size, source2.size)
    freq = freq2

    # Mix the sources into the simulated signals recorded by the mics.
    rec1 = 0.75 * source1[:n] + 0.25 * source2[:n]
    rec2 = 0.60 * source1[:n] + 0.40 * source2[:n]

    # Convert to 16 bit integers.
    out1 = (2000 * rec1).astype(np.int16)
    out2 = (2000 * rec2).astype(np.int16)

    wavfile.write('wav/mic1.wav', freq, out1)
    wavfile.write('wav/mic2.wav', freq, out2)
