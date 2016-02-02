
from scipy.interpolate import Rbf
from numpy import hypot, mgrid
from scipy import rand
from scipy.special import j0

x = rand(50)*10 - 5
y = rand(50)*10 - 5
z = j0(hypot(x,y))
newfunc = Rbf(x,y,z)
xx,yy = mgrid[-5:5:100j, -5:5:100j]

zz = newfunc(xx,yy)
ztrue = j0(hypot(xx,yy))

from mayavi import mlab

mlab.figure(1)
mlab.clf()
mlab.surf(xx,yy,ztrue*5)
mlab.title('True')
mlab.figure(2)
mlab.clf()
mlab.surf(xx,yy,zz*5)
mlab.points3d(x,y,z*5, scale_factor=0.5)
mlab.title('Interpolation')
mlab.figure(3)
mlab.clf()
mlab.surf(xx,yy,(zz-ztrue)*5)
mlab.axes()
mlab.title('Difference')

err = abs(zz-ztrue)
print err.min(), err.max(), err.mean(), err.std()

