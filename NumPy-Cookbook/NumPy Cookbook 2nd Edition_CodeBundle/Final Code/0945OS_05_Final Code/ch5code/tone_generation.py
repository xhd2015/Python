import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

RATE = 44100
DTYPE = np.int16

# Generate sine wave
def generate(freq, amp, duration, phi):
 t = np.linspace(0, duration, duration * RATE)
 data = np.sin(2 * np.pi * freq * t + phi) * amp

 return data.astype(DTYPE)

# Initialization
NTONES = 89
amps = 2000. * np.random.random((NTONES,)) + 200.
durations = 0.19 * np.random.random((NTONES,)) + 0.01
keys = np.random.random_integers(1, 88, NTONES)
freqs = 440.0 * 2 ** ((keys - 49.)/12.)
phi = 2 * np.pi * np.random.random((NTONES,))

tone = np.array([], dtype=DTYPE) 

# Compose 
for i in xrange(NTONES):
   newtone = generate(freqs[i], amp=amps[i], duration=durations[i], phi=phi[i])
   tone = np.concatenate((tone, newtone))

scipy.io.wavfile.write('generated_tone.wav', RATE, tone)

# Plot audio data
plt.plot(np.linspace(0, len(tone)/RATE, len(tone)), tone)
plt.show()
