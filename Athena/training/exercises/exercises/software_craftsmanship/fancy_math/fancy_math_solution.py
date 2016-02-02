""" Test Driven Development Example

    Write a function called `slope` that calculates the slope
    between two points.  A point is specified by a two element
    sequence of (x,y) coordinates. 
    
        >>> pt1 = [0.0, 0.0]
        >>> pt2 = [1.0, 2.0]
        >>> slope(pt1, pt2)
        2.0
    
    Use Test Driven Development.  Write your tests first in
    a separate file called tests_fancy_math.py.  
    
    Run your tests using the "nosetests" shell command.  You can
    do this by changing to the "slope" directory where your 
    fancy_math.py is defined and running "nosetests".  From IPython,
    you can run it like this:
    
       In [1]: cd <someplace>/exercises/slope
       In [2]: !nosestests
       ...
       --------------------------------------------------
       Ran 3 tests in 0.157s
       
    If you would like to see more verbose output, use the "-v"
    option:

       In [3]: !nosetests -v
       test_fancy_math.test_slope_xxx ... ok
       test_fancy_math.test_slope_yyy ... ok
       ...

    By default, nose captures all output and does not print it
    to the screen.  If you would like to see the output of print
    statements, use the "-s" flag.                    
"""
from __future__ import division
from numpy import Inf

def slope(pt1, pt2):
    dy = pt2[1] - pt1[1]
    dx = pt2[0] - pt1[0]
    try:
        slope = dy/dx
    except ZeroDivisionError:
        if dy > 0:
            slope = Inf
        else:
            slope = -Inf
            
    return slope
