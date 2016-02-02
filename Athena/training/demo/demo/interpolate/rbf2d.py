
from scipy.interpolate import Rbf
from numpy import hypot, mgrid
from scipy.special import j0

x,y = mgrid[-5:6,-5:6]
z = j0(hypot(x,y))
newfunc = Rbf(x,y,z)
xx,yy = mgrid[-5:5:100j, -5:5:100j]

zz = newfunc(xx,yy)

from mayavi import mlab

mlab.figure(1)
mlab.clf()
mlab.surf(x,y,z*5)
mlab.title('Data (z)')
mlab.figure(2)
mlab.clf()
mlab.surf(xx,yy,zz*5)
mlab.points3d(x,y,z*5, scale_factor=0.5)
mlab.title('Interpolation (zz)')


