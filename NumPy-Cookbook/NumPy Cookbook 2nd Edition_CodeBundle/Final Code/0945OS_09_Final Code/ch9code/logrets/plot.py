from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy as np
from log_returns import logrets
import matplotlib.pyplot as plt

today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo('AAPL', start, today)
close =  np.array([q[4] for q in quotes])
plt.plot(logrets(close))
plt.title('Logreturns of AAPL for the previous year')
plt.xlabel('Days')
plt.ylabel('Log returns')
plt.grid()
plt.show()
