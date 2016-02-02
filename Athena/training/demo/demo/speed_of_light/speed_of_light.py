# Numeric library imports
from numpy import arange, loadtxt
from scipy import stats

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

# histogram the measured velocities.
bin_counts, min_val, width, outside = stats.histogram(measured_velocity,
                                                      numbins=30)
print 'min val:', min_val

# For plot, we want to know the velocities for each bin.
binned_velocity = min_val + arange(len(bin_counts))*width
print binned_velocity

# Plot a bar plot of the histogrammed data.
pylab.hold(False)

pylab.bar(binned_velocity, bin_counts, width=width)

pylab.xlabel("velocity (1e8 m/s)")
pylab.ylabel("counts")
pylab.title("Newcoumbs Speed of Light Measurement Histogram")

pylab.hold(True)

# Put a vertical line in where the actual velocity is.
actual = 2.99792458
pylab.plot([actual, actual], [0,max(bin_counts)],'r-', linewidth=2)
pylab.axis('auto')

# Ensure that the plot is shown.
pylab.show()
