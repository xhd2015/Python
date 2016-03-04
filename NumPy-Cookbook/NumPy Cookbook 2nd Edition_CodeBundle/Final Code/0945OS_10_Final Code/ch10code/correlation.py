from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import finance
import numpy as np

# 2011 to 2012
start = datetime(2011, 01, 01)
end = datetime(2012, 01, 01)

symbols = ["AA", "AXP", "BA", "BAC", "CAT"]

quotes = [finance.quotes_historical_yahoo(symbol, start, end, asobject=True)
          for symbol in symbols]

close = np.array([q.close for q in quotes]).astype(np.float)
dates = np.array([q.date for q in quotes])

data = {}

for i, symbol in enumerate(symbols):
   data[symbol] = np.diff(np.log(close[i]))

# Convention: import pandas as pd
df = pd.DataFrame(data, index=dates[0][:-1], columns=symbols)
 
 
print(df.corr())
df.plot()
plt.legend(symbols)
plt.show()

#           AA       AXP        BA       BAC       CAT
#AA   1.000000  0.768484  0.758264  0.737625  0.837643
#AXP  0.768484  1.000000  0.746898  0.760043  0.736337
#BA   0.758264  0.746898  1.000000  0.657075  0.770696
#BAC  0.737625  0.760043  0.657075  1.000000  0.657113
#CAT  0.837643  0.736337  0.770696  0.657113  1.000000
