""" 
Wind Statistics
----------------

This exercise is an alternative version of the Numpy exercise but this time we 
will be using pandas for all tasks. The data have been modified to contain some 
missing values identified by -0.00 or NaN depending on whether the measurement 
couldn't be trusted or whether no data was collected. Using pandas should make 
this exercise easier, in particular for the bonus question.


Of course, you should be able to perform all of these operations without using a 
for loop or other looping construct.


Topics: Pandas, time-series

1. The data in 'wind.data' has the following format::

        Yr Mo Dy   RPT   VAL   ROS   KIL   SHA   BIR   DUB   CLA   MUL   CLO   BEL   MAL
        61  1  1 15.04 14.96 13.17  9.29 -0.00  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71   NaN 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25   NaN  8.50  7.67 12.75 12.71
   
   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.
   
   Use the 'read_table' function from pandas to read the data into
   a DataFrame. Make sure to convert all missing values (NaN and -0.00 to 
   np.nan).
      
2. Replace the first 3 columns by a proper datetime index, created manually.

3. Compute how many values are missing for each location over the entire record. 
   They should be ignored in all calculations below. Compute how many 
   non-missing values there are in total.

4. Calculate the mean windspeeds of the windspeeds over all the locations and 
   all the times (a single number for the entire dataset). 

5. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers 
   for each location)

6. Calculate the min, max and mean windspeed and standard deviations of the windspeeds
   across all the locations at each day (a different set of numbers for each day)

7. Find the average windspeed in January for each location.  Treat
   January 1961 and January 1962 both as January.

8. Downsample the record to a yearly, monthly frequency and weekly frequency for 
   each location.

9. Plot linearly and with a candle plot the monthly data for each location.

(Used to be a bonus)

10. Calculate the mean windspeed for each month in the dataset.  Treat
    January 1961 and January 1962 as *different* months.
   
11. Calculate the min, max and mean windspeeds and standard deviations of the
    windspeeds across all locations for each week (assume that the first week
    starts on January 1 1961) for the first 52 weeks. 

Notes
~~~~~

This solution has been tested with Pandas version 0.7.3. 

The original data from which these were derived were analyzed in detail in the 
following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.

"""

from pandas import read_table
from datetime import datetime

# 1.
wind_data_df = read_table('wind.data', sep = '\s*', header = 1)

# 2.
# Extract the data part
data_df = wind_data_df.ix[:,3:]

# the fully generic way
index = []
for row in range(len(data_df)):
    year = int(1900+wind_data_df.ix[row,0])
    month = int(wind_data_df.ix[row,1])
    day = int(wind_data_df.ix[row,2])
    index.append(datetime(year, month, day))
data_df.index = index

print "Data:", data_df

# Non-missing values at each location
print "3. Number of non-missing values for each location:"
print data_df.count()
non_null_count = data_df.count().sum()
print "There are {0} non-missing values in the entire dataset".format(non_null_count)
print 

print '4. Mean over all values'
total = data_df.sum().sum()
print '  mean:', total/non_null_count
print

print '5. Statistics over all days at each location'
print '  min:', data_df.min()
print '  max:', data_df.max()
print '  mean:', data_df.mean()
print '  standard deviation:', data_df.std()
print

print '6. Statistics over all locations for each day'
print '  min:', data_df.min(axis=1)
print '  max:', data_df.max(axis=1)
print '  mean:', data_df.mean(axis=1)
print '  standard deviation:', data_df.std(axis=1)
print 

monthly_grouped = data_df.groupby(lambda d: d.month)
monthly_means = monthly_grouped.mean()
print '7. Mean wind speed for January in each location'
print monthly_means.ix[1]
print 

# Downsample the data to yearly, monthly and weekly data
print "8. Downsampled data:"
# To avoid loosing the first few days, identify which day of the week the first 
# day corresponds to
yearly_group = data_df.groupby(lambda x: x.year)
print "Yearly:", yearly_group.mean()

monthly_group = data_df.groupby(lambda x: (x.year,x.month))
print "Monthly:", monthly_group.mean()

# For a given entry in the index, identify which week it belongs to (multiple of
# 7).
which_week = lambda x: (x-data_df.index[0]).days / 7
weekly_group = data_df.groupby(which_week)
print "Weekly data:", weekly_group.mean()
print 

# 9. Plots
monthly_data = monthly_group.mean()
from matplotlib import pyplot
monthly_data.plot()
# Force this plot to happen in a separate figure
pyplot.figure()
monthly_data.boxplot()
pyplot.show()

# 10. This is just another way to group records:
unique_monthly_grouped = data_df.groupby(lambda d: (d.month, d.year))
print '10. Mean wind speed for each month in each location'
print unique_monthly_grouped.mean()
print 
  

# 11. Weekly stats over the first year
first_year = data_df.ix[:52*7,:]
weekly_first_year = first_year.groupby(which_week)
stats = weekly_first_year.apply(lambda x: x.describe())
import pandas
pandas.set_printoptions(max_rows=500, max_columns = 15, notebook_repr_html=False)
print stats
