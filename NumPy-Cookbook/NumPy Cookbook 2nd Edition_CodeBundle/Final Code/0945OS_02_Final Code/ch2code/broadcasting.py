import scipy.io.wavfile
import matplotlib.pyplot as plt
import urllib2
import numpy as np

# Download audio file
response = urllib2.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
print(response.info())
WAV_FILE = 'smashingbaby.wav'
filehandle = open(WAV_FILE, 'w')
filehandle.write(response.read())
filehandle.close()
sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
print("Data type", data.dtype, "Shape", data.shape)

# Plot values original audio
plt.subplot(2, 1, 1)
plt.title("Original")
plt.plot(data)

# Create quieter audio
newdata = data * 0.2
newdata = newdata.astype(np.uint8)
print("Data type", newdata.dtype, "Shape", newdata.shape)

# Save quieter audio file
scipy.io.wavfile.write("quiet.wav",
    sample_rate, newdata)

# Plot values quieter file
plt.subplot(2, 1, 2)
plt.title("Quiet")
plt.plot(newdata)

plt.show()
