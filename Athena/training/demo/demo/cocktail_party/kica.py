
import numpy as np
from scipy.linalg import sqrtm, svd

def kica(xx):

    # MATLAB code (see http://cs.nyu.edu/~roweis/kica.html):
    # % W = kica(xx);
    # >> yy = sqrtm(inv(cov(xx'))) * (xx-repmat(mean(xx,2),1,size(xx,2)));
    # >> [W,ss,vv] = svd((repmat(sum(yy.*yy,1),size(yy,1),1).*yy) * yy');

    # For readability, we won't try to implement it in just two lines.
    xxm = xx - xx.mean(axis=1).reshape(-1, 1)
    a = sqrtm(np.linalg.inv(np.cov(xx))).real
    yy = np.dot(a, xxm)
    ss = (yy**2).sum(axis=0)
    b = ss * yy
    c = np.dot(b, yy.T)
    [W, ss, vvt] = svd(c)

    return W, yy
