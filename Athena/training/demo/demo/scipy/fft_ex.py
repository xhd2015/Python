from numpy.fft import fftfreq, fft, fftshift
from numpy import pi, exp
import pylab  as plt


n = fftfreq(128)*128
f = fftfreq(128)
ome = 2*pi*f
x = (0.9)**abs(n)
X = fft(x)
z = exp(1j*ome)
Xexact = (0.9**2 - 1)/0.9*z / (z-0.9) / (z-1/0.9)
plt.plot(fftshift(f), fftshift(X.real),'r-',
         fftshift(f), fftshift(Xexact.real),'bo')
plt.title('Fourier Transform Example')
plt.xlabel('Frequency (cycles/s)')
plt.xlim(-0.6,0.6)
plt.show()
# Need a legend!
