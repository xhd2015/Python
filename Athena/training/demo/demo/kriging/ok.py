"""
This module shows how ordinary kriging can be implemented using numpy.
"""

#
# Implement ordinary kriging with numpy.
#
# Author: Warren Weckesser, Enthought, Inc.
#

import numpy as np
from numpy.linalg import solve


# XXX Unify the arguments of the variogram functions?
#     Perhaps express them all in terms of nugget, sill and range.

def exponential(h, c0=0.0, c1=1.0, a=1.0):
    v = c0 + c1 * (1.0 - np.exp(-3.0 * np.abs(h) / a))
    v[h == 0] = 0
    return v


def spherical(h, rng=1.0, nugget=0.0, sill=1.0):
    hn = np.asarray(h) / rng
    v = np.where(h > rng,
                    sill,
                    nugget + (sill - nugget) * (1.5 * hn - 0.5 * hn ** 3))
    v[h == 0] = 0
    return v


def okweights(x, obs, sv):
    """
    Compute the weights for ordinary kriging.

    Parameters
    ----------
    x : ndarray, shape (m, d)
        The coordinates at which the function is to be interpolated.
    obs : ndarray, shape (n, d)
        The coordinates of the known data points.
    sv : callable
        The semivariance function.

    Returns
    -------
    w : ndarray, shape (n, m)
       The weight for each point in x.
    lambda_ : ndarray, shape ???
       The Lagrange multiplier.
    v : ndarray, shape XXX
       The variances.  These are simply sv(dist) for each dist that is a
       distance from a known point to a point in x.
    """
    x = np.atleast_2d(x)
    obs = np.atleast_2d(obs)
    if x.shape[1] != obs.shape[1]:
        raise ValueError("x and obs must have the same second dimension.")

    # Number of points to be interpolated.
    nints = x.shape[0]
    # Number of observations.
    nobs = obs.shape[0]
    # Put the observed coordinates and the coordinates to be kriged
    # into one array, obs_ext.
    obs_ext = np.vstack((obs, x))
    # Compute the distance matrix.
    dist = np.sqrt(((obs_ext - obs[:, np.newaxis, :]) ** 2).sum(axis=-1))
    # gam is the array of semivariance values.
    gam = sv(dist)
    # Form the block matrix
    #         [ gam[:,:nobs]  |  1 ]
    #     A = [---------------+----]
    #         [      1        |  0 ]
    # where gam[:, :nobs] is the square matrix of semivariances among
    # the observed coordinates.
    A1 = np.vstack((gam[:, :nobs], np.ones(nobs)))
    A = np.hstack((A1, np.ones((nobs + 1, 1))))
    A[-1, -1] = 0
    #     [ gam[:, nobs:] ]
    # b = [---------------]
    #     [       1       ]
    b = np.vstack((gam[:, nobs:], np.ones(nints)))
    # Solve the matrix equation A*w = b for w.
    # Then w[:-1] holds the kriging weights, and w[-1]
    # holds the Lagrange multiplier.
    w = solve(A, b)
    return w[:-1], w[-1], b[:-1]


def okrige(x, obs, values, sv):
    """
    Apply ordinary kriging to the data with coordinates `obs` and
    corresponding values `values`.  `sv` must be a callable that
    computes the semivariance of a given distance.
    """
    # Ensure that we have numpy arrays.
    x = np.atleast_2d(x)
    obs = np.atleast_2d(obs)
    values = np.asarray(values)

    weights, lambda_, v = okweights(x, obs, sv)

    est_value = np.dot(values, weights)
    est_var = (v * weights).sum(axis=0) + lambda_ * np.ones(x.shape[0])

    return est_value, est_var
