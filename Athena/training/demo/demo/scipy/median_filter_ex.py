from numpy import float32
from pylab import imshow, figure, show
from scipy import signal, lena

figure()
lena = lena()
lena = lena.astype(float32)
imshow(lena)

figure()
fl = signal.medfilt2d(lena,[15,15])
imshow(fl)

show()
