from datetime import datetime
#import urllib2
import numpy as np
import matplotlib.pyplot as plt


# Structured array data type for the numpy array.
dt = np.dtype([('time', np.datetime64),
               ('temp', np.float32),
               ('salinity', np.float32),
               ('ph', np.float32),
               ('depth', np.float32)])

# Uncomment the next two lines (and comment the line 'f = open(...)') to
# get the data directly from the web.
#url = "http://lighthouse.tamucc.edu/pd?stnlist=072&serlist=wtp%2Csal%2Cph%2Cdth&when=03.30.2012-04.06.2012&whentz=CST6CDT&-action=c&unit=metric&elev=stnd"
#f = urllib2.urlopen(url)
f = open("data.txt")

# Timestamp format.
fmt = "%Y%j+%H%M"

# Use genfromtxt instead of loadtxt.  Several rows contain the string 'NA',
# and genfromtxt will automatically convert these to NaN.
data = np.genfromtxt(f, dtype=dt, converters={0: lambda s: datetime.strptime(s, fmt)})
f.close()


# Plot some of the data...

fig = plt.figure()

# To plot the np.datetime64 field in matplotlib, we convert it to
# the 'object' type.  This will result in an array of datetime.datetime
# objects, which matplotlib understands.
plt.plot(data['time'].astype(object), data['depth'], 'b.-')
fig.autofmt_xdate()
plt.grid(True)

plt.show()
