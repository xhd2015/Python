
import numpy as np

from ok import exponential, okrige


def example1():
    """
    This is the data from the example at
    http://www.cee.vt.edu/ewr/environmental/teach/smprimer/kriging/kriging.html
    (That URL no longer exists; you'll have to use the "wayback machine" at
    http://web.archive.org to view it.)
    The web page shows the result for the points (3,2) and (4,4).
    """
    obs = np.array([[1, 2], [4, 1], [6, 4]])
    elev = np.array([150, 110, 140])
    # Points at which to estimate the elevation.
    p = [[3, 2], [4, 4]]

    est_elev, est_var = okrige(p, obs, elev, lambda x: 4 * x)

    print "Kriging Example 1"
    print "Point   Est. elevation   Est. variance"
    print "--------------------------------------"
    fmt = "{:2d},{:2d}     {:7.3f}          {:7.3f}"
    for pt, el, var in zip(p, est_elev, est_var):
        print fmt.format(pt[0], pt[1], el, var)

    # Values from the web page:
    #    128.9  6.70
    #    138.6  10.4  (inferred the variance from the error interval: +-6.45)


def example2():
    """
    This example is from Chapter 12 (p. 290-296) of "An Introduction to Applied
    Geostatistics" by Isaaks and Srivastava (Oxford, 1989).
    """

    # Data from Table 12.1 (p. 291).  We need only x, y and v.
    data = np.array([[61, 139, 477],
                     [63, 140, 696],
                     [64, 129, 227],
                     [68, 128, 646],
                     [71, 140, 606],
                     [73, 141, 791],
                     [75, 128, 783]], dtype=np.float64)

    coords = data[:, :2]
    values = data[:, 2]

    # Points at which to estimate the elevation.
    # We have just one point for this example.
    p = np.array([[65, 137]], dtype=np.float64)

    semivar = lambda x: exponential(x, c0=0, c1=10, a=10)
    est_value, est_var = okrige(p, coords, values, semivar)

    print "Kriging Example 2"
    print 'Example from "An Introduction to Applied Geostatistics"'
    print 'by Isaaks and Srivastava (Oxford, 1989)'
    print "             okrige    book"
    print "Value:    {:9.4f}   592.7".format(est_value[0])
    print "Variance: {:9.4f}     8.96".format(est_var[0])


if __name__ == "__main__":
    print "-" * 75
    example1()
    print "-" * 75
    example2()
    print "-" * 75
