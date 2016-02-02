
from __future__ import with_statement

from numpy import fromregex
import os
import datetime
from pylab import plot_date
import urllib2, string


# Download from Google with 
# wget -O <name>.csv -r "http://www.google.com/finance/historical?q=NASDAQ:<NAME>&startdate=Jan+1,1990&enddate=Aug+20,2008&output=csv"

# Download from Yahoo with
#  to indicate start date:
#    a -- Month number-1  
#    b -- Month day
#    c -- Year
#  to indicate end date:
#    d -- Month number-1
#    e -- Month day
#    f -- Year
# wget -O <name>.csv -r "http://ichart.finance.yahoo.com/table.csv?s=<NAME>&a=00&b=1&c=1970&d=07&e=21&f=2009&g=d&ignore=.csv"

# Download from yahoo the stock named name --- assumes wget is installed on the system
def yh_download(name):
    os.system('wget -O %s.csv -r "http://ichart.finance.yahoo.com/table.csv?s=%s&a=00&b=1&c=1970&d=07&e=21&f=2009&g=d&ignore=.csv"' % (name, name.upper()))

def yh_download(name, start=(1,1,1970), end=(8,21,2009)):
    a,b,c = start
    d,e,f = end
    a = a-1
    d = d-1
    symb = name.upper()
    tmpl = string.Template("http://table.finance.yahoo.com/table.csv?s=$symb&a=$a&b=$b&c=$c&d=$d&e=$e&f=$f&g=d&ignore=.csv")
    obj = urllib2.urlopen(tmpl.substitute(locals()))
    fid = open("%s.csv" % (name,), 'w')
    fid.write(obj.read())
    fid.close()
    obj.close()
    
# Return a date array which can be used with matplotlib's plot_date
def yh_convert_date(arr):
    start = datetime.date(1,1,1)
    return [(datetime.date(x,y,z) - start).days for x, y, z in zip(arr['year'], arr['month'], arr['day'])]

# Plot stock with date
def plot_stock(arr, field='adj_close', **kwd):
    dates = yh_convert_date(arr)
    plot_date(dates, arr[field], **kwd)
     
gf_regex = r"(\d{1,2})-([A-Za-z]{3})-(\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+)\n"
gf_dtype = [('day', 'i2'), ('month', 'S3'), ('year', 'i4'), ('open', 'f4'), ('high', 'f4'), ('low', 'f4'), ('close', 'f4'), ('volume', 'i4')]

yf_regex = r"(\d{4})-(\d{2})-(\d{2}),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+),(\d+[.]\d+)"
yf_dtype = [('year', 'i4'), ('month', 'i2'), ('day', 'i2'), ('open', 'f4'), ('high', 'f4'), ('low', 'f4'), ('close', 'f4'), ('volume', 'i4'), ('adj_close', 'f4')]


def load_quote(quote, overwrite=False):
    filename = "%s.csv" % quote
    if overwrite is True or \
      (overwrite is False and not os.path.exists(filename)):
        try:
            yh_download(quote)
        except urllib2.HTTPError, e:
            print "Error with %s" % quote
            return None        
    return fromregex(filename, yf_regex, yf_dtype)
    

def old_method():
    names = ['yhoo', 'goog', 'ibm', 'ge', 'msft', 'aapl', 'ebay', 'dell', 'csco', 'siri']
    quotes = dict()
    for name in names:
        arr = load_quote(name)
        quotes[name] = arr
    return quotes

def load_eurostoxx50(overwrite=False):    
    """
    Loads the EuroStoxx 50 index components and returns a dictionnary
    """
    stocks = ["ABI.BR", "ACA.PA", "AGN.AS", "AI.PA", "ALO.PA", "ALV.DE",
              "BAS.DE", "BAYN.DE", "BBVA.MC", "BN.PA", "BNP.PA", "CA.PA", "CRG.IR", "CS.PA",
              "DAI.DE", "DB1.DE", "DBK.DE", "DG.PA", "DTE.DE", "ENEL.MI", "ENI.MI",
              "EOAN.DE", "FP.PA", "FTE.PA", "G.MI", "GLE.PA", "GSZ.PA", "IBE.MC", "INGA.AS",
              "ISP.MI", "MC.PA", "MUV2.DE", "NOK1V", "OR.PA", "PHIA.AS", "REP.MC", "RWE.DE",
              "SAN.MC", "SAN.PA", "SAP.DE", "SGO.PA", "SIE.DE", "SU.PA", "TEF.MC", "TIT.MI",
              "UCG.MI", "UL.PA", "UNA.AS", "VIV.PA"]
    quotes = dict()
    for name in stocks:
            print "Loading %s" % name
            arr = load_quote(name, overwrite)
            quotes[name] = arr
    return quotes

def load_sandp_500():
    """
    Load the daily value of the S&P500 and returns a structured array
    """
    quote = "^GSPC" 
    return load_quote(quote)
    



