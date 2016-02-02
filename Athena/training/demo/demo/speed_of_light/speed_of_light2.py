# This version is simpler because it uses the 'hist' plotting command 
# instead of doing the math ourselves.  It also uses the axvline
# to generate the vertical line for the actual results.

# Numeric library imports
from numpy import arange, loadtxt

# Plotting imports
from matplotlib import pylab

# Distance light traveled in Newcoumbs experiment
distance = 7400.0

# Read the measurements from the data file.
# There are a number of comments at the top of the file marked with "#"
measured_time = loadtxt('speed_of_light.dat',comments="#")

# measurements were in nanseconds difference from 24800 ns.
measured_time += 24800.0

# Convert measured times to measured velocities.
measured_velocity = distance/measured_time*10.0  # m/ns * 10 == 1e8m/s

# Plot a bar plot of the histogrammed data.
pylab.hold(False)

pylab.hist(measured_velocity, bins=30)

pylab.xlabel("velocity (1e8 m/s)")
pylab.ylabel("counts")
pylab.title("Newcoumbs Speed of Light Measurement Histogram")

# Put a vertical line in where the actual velocity is.
actual = 2.99792458
pylab.axvline(actual, color='r', linewidth=2, hold=True)
pylab.axis('auto')

# Ensure that the plot is shown.
pylab.show()
