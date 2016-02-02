from numpy import exp, cos, linspace
from traits.api import HasTraits, Float, Array, Property


class DampedOsc(HasTraits):
    """Computes the function y = a * exp(-b*x) * cos(omega * x + phase)."""

    # The 'a' parameter.
    a = Float(1.0)

    # The 'b' parameter.
    b = Float(0.1)

    # The 'omega' parameter (quasi-frequency, in radians/time)
    omega = Float(1.0)

    # The 'phase' parameter.
    phase = Float(0.0)

    # Values at which to evaluate the function.
    x = Array

    # The values of the functions at `x`.
    y = Property(depends_on=['a', 'b', 'omega', 'phase', 'x'])

    def _get_y(self):
        y = (self.a * exp(-self.b * self.x) *
             cos(self.omega * self.x + self.phase))
        return y

    def _x_default(self):
        return linspace(0.0, 20.0, 501)


if __name__ == "__main__":
    # If run as a script, create an instance of DampedOsc, and print
    # some function values.
    osc = DampedOsc()
    osc.x = linspace(0, 1, 5)
    print "x:",
    for x in osc.x:
        print "{:6.3f}".format(x),
    print
    print "y:",
    for y in osc.y:
        print "{:6.3f}".format(y),
