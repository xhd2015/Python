""" This module provides functions for interpolation.  They are 
    based on numpy arrays.    
"""
import numpy

def interp(x, xp, fp, left=None, right=None):
    """
    One-dimensional linear interpolation.

    Returns the one-dimensional piecewise linear interpolant to a function
    with given values at discrete data-points.

    Notes
    =====
    Does not check that the x-coordinate sequence C{xp} is increasing.
    If C{xp} is not increasing, the results are nonsense.
    A simple check for increasingness is::

        np.all(np.diff(xp) > 0)
            
    Examples
    ========
    
        >>> xp = [1, 2, 3]
        >>> fp = [3, 2, 0]
        >>> np.interp(2.5, xp, fp)
        1.0
        >>> np.interp([0, 1, 1.5, 2.72, 3.14], xp, fp)
        array([ 3. ,  3. ,  2.5,  0.56,  0. ])
        >>> UNDEF = -99.0
        >>> np.interp(3.14, xp, fp, right=UNDEF)
        -99.0
    
    @param x : array_like.
        The x-coordinates of the interpolated values.

    @param xp : 1-D sequence of floats.
        The x-coordinates of the data points, must be increasing.

    @param fp : 1-D sequence of floats.
        The y-coordinates of the data points, same length as C{xp}.

    @param left : float, optional.
        Value to return for C{x < xp[0]}, default is C{fp[0]}.

    @param right : float, optional.
        Value to return for C{x > xp[-1]}, defaults is C{fp[-1]}.

    @return: float or ndarray.
        The interpolated values, same shape as C{x}.

    @raise ValueError : If C{xp} and C{fp} have different length
    """
    pass
    
