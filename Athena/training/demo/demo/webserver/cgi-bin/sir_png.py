#!/Library/Frameworks/Python.framework/Versions/Current/bin/python

# NOTE:
# Change the first line of this file to one of the
# following, depending on which OS you are using. Modify
# the path to the python executable command as to match
# your installation; the following are just examples.
#
# Windows with EPD 7.1:
#!C:\Python27\python.exe
#
# Linux with EPD 7.0:
#!/home/warren/EPD/epd-7.0-2-rh5-x86_64/bin/python
#
# Mac OS X EPD:
#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
#

#
# sir_png.py
#
# This is a CGI program that generates a PNG file containing a plot
# of a solution to the SIR differential equations.
#
# Warren Weckesser
# www.enthought.com
#

import sys
import cgi
from math import isnan

import numpy as np
from scipy.integrate import odeint

from sir import SIR, SIR_jac
from sir_plot import plot_solution, bad_values_canvas


def get_float_value(form, name):
    """
    Find the key name in the form, and try to convert its
    value to a floating point number. The return value is
    either the floating point value, or np.NaN if either the
    form did not contain the name, or the value could not be
    converted to a floating point number.
    """
    try:
        value = float(form[name].value)
    except Exception:
        value = np.NaN
    return value


def print_content_lines():
    print 'Content-type: image/png\n'


def main():
    print_content_lines()
    form = cgi.FieldStorage()

    # Get the parameters and initial conditions from the CGI form.
    duration = get_float_value(form, 'duration')
    alpha = get_float_value(form, 'alpha')
    gamma = get_float_value(form, 'gamma')
    S0 = get_float_value(form, 'S0')
    I0 = get_float_value(form, 'I0')
    R0 = get_float_value(form, 'R0')

    if any([isnan(duration), isnan(alpha), isnan(gamma),
            isnan(S0), isnan(I0), isnan(R0)]):
        # One of the numeric entries was invalid.
        # Create a canvas containing an error message.
        canvas = bad_values_canvas()
        canvas.print_figure(sys.stdout)
        sys.stdout.close()
        return        
 
    # Create the time samples for the output of the ODE solver.
    N = 250  # Hardwired number of points.
    t = np.linspace(0.0, duration, N)

    # Initial conditions S(0), I(0) and R(0)
    y = [S0, I0, R0]

    # Call the SciPy ODE solver.
    ysol = odeint(SIR, y, t, args=(alpha, gamma), Dfun=SIR_jac,
                  atol=1.0e-8, rtol=1.0e-6)

    canvas = plot_solution(t, ysol)
    canvas.print_figure(sys.stdout)


main()
