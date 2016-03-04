from __future__ import print_function
import numpy as np
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import matplotlib.pyplot as plt


def get_close(ticker):
   today = date.today()
   start = (today.year - 1, today.month, today.day)

   quotes = quotes_historical_yahoo(ticker, start, today)

   return np.array([q[4] for q in quotes])


close = get_close('AAPL')

triples = np.arange(0, len(close), 3)
print("Triples", triples[:10], "...")

signs = np.ones(len(close))
print("Signs", signs[:10], "...")

signs[triples] = -1
print("Signs", signs[:10], "...")

ma_log = np.ma.log(close * signs)
print("Masked logs", ma_log[:10], "...")

dev = close.std()
avg = close.mean()
inside = np.ma.masked_outside(close, avg - dev, avg + dev)
print("Inside", inside[:10], "...")

plt.subplot(311)
plt.title("Original")
plt.plot(close)

plt.subplot(312)
plt.title("Log Masked")
plt.plot(np.exp(ma_log))

plt.subplot(313)
plt.title("Not Extreme")
plt.plot(inside)

plt.tight_layout()
plt.show()
