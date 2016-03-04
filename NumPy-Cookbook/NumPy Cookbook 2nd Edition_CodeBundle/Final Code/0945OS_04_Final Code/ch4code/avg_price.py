from __future__ import print_function
import urllib2
import re
import time
import numpy as np

prices = np.array([])

for i in xrange(3):
   req = urllib2.Request('http://finance.google.com/finance/info?client=ig&q=AAPL')
   req.add_header('User-agent', 'Mozilla/5.0')
   response = urllib2.urlopen(req)
   page = response.read()
   m = re.search('l_cur" : "(.*)"', page)
   prices = np.append(prices, float(m.group(1)))
   avg = prices.mean()
   stddev = prices.std()
 
   devFactor = 1
   bottom = avg - devFactor * stddev
   top = avg + devFactor * stddev
   timestr = time.strftime("%H:%M:%S", time.gmtime())
 
   print(timestr, "Average", avg, "-Std", bottom, "+Std", top)
   time.sleep(60)
