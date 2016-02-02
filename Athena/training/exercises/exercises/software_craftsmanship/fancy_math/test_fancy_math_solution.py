from numpy import Inf
from nose.tools import assert_almost_equal, assert_equal

from fancy_math_solution import slope

def test_slope_float():
    pt1 = [0.0, 0.0]
    pt2 = [1.0, 2.0]
    s = slope(pt1, pt2)
    assert_almost_equal(s, 2)

    pt1 = [0.0, 0.0]
    pt2 = [-2.0, 1.0]
    s = slope(pt1, pt2)
    assert_almost_equal(s, -0.5)
    
def test_slope_integer():
    """ Integer division has the potential to break the slope function.
    """
    pt1 = [0, 0]
    pt2 = [2, 1]
    s = slope(pt1, pt2)
    assert_almost_equal(s, 0.5)
    
def test_slope_infinite():
    """ Test for infinite slope function.
    """
    pt1 = [0, 0]
    pt2 = [0, 1]
    s = slope(pt1, pt2)
    assert_equal(s, Inf)
    
    pt1 = [0, 0]
    pt2 = [0, -1]
    s = slope(pt1, pt2)
    assert_equal(s, -Inf)        