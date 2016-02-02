__author__ = 'Plamen'

from matplotlib.finance import quotes_historical_yahoo_ochl

ticker='IBM'
begdate=(2008,10,1)
enddate=(2013,11,30)
p = quotes_historical_yahoo_ochl(ticker, begdate, enddate,asobject=True,adjusted=True)

from matplotlib.pyplot import *
plot([1,2,3,10])
xlabel("x- axis")
ylabel("my numbers")
title("my figure")
show()