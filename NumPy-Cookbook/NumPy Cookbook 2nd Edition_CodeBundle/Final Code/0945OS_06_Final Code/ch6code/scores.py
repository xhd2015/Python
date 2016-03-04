from __future__ import print_function
import numpy as np
from matplotlib.finance import quotes_historical_yahoo
from datetime import date

tickers = ['MRK', 'T', 'VZ']

def get_close(ticker):
   today = date.today()
   start = (today.year - 1, today.month, today.day)

   quotes = quotes_historical_yahoo(ticker, start, today)

   return np.array([q[4] for q in quotes])


weights = np.recarray((len(tickers),), dtype=[('symbol', np.str_, 16), 
   ('stdscore', float), ('mean', float), ('score', float)])

for i, ticker in enumerate(tickers):
   close = get_close(ticker)
   logrets = np.diff(np.log(close))
   weights[i]['symbol'] = ticker
   weights[i]['mean'] = logrets.mean()
   weights[i]['stdscore'] = 1/logrets.std()
   weights[i]['score'] = 0

for key in ['mean', 'stdscore']:
   wsum = weights[key].sum()
   weights[key] = weights[key]/wsum

weights['score'] = (weights['stdscore'] + weights['mean'])/2
weights['score'].sort()

for record in weights:
   print("%s,mean=%.4f,stdscore=%.4f,score=%.4f" % (record['symbol'], record['mean'], record['stdscore'], record['score']))
