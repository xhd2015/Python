from __future__ import print_function
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import finance
import numpy as np

# Download AAPL data for 2011 to 2012
start = datetime(2011, 01, 01)
end = datetime(2012, 01, 01)

symbol = "AAPL"
quotes = finance.quotes_historical_yahoo(symbol, start, end, asobject=True)

# Create date time index
dt_idx = pandas.DatetimeIndex(quotes.date)

#Create data frame
df = pandas.DataFrame(quotes.close, index=dt_idx, columns=[symbol])

# Resample with monthly frequency
resampled = df.resample('M', how=np.mean)
print(resampled) 
 
# Plot
df.plot()
plt.title('AAPL prices')
plt.ylabel('Price')

resampled.plot()
plt.title('Monthly resampling')
plt.ylabel('Price')
plt.grid(True)
plt.show()
