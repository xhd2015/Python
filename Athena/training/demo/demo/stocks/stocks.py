
from numpy import fromregex
import os
import datetime
from pylab import plot_date


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

def yh_download(name, start=(1,1,1970), end=None):
    import urllib2, string
    if isinstance(start, datetime.datetime):
        start = [getattr(start, x) for x in ['month', 'day', 'year']]
    a,b,c = start
    if end is None:
        end = datetime.datetime.now()
    if isinstance(end, datetime.datetime):
        end = [getattr(end, x) for x in ['month', 'day', 'year']]
    d,e,f = end
    a = a-1
    d = d-1
    symb = name.upper()
    tmpl = string.Template("http://ichart.finance.yahoo.com/table.csv?s=$symb&a=$a&b=$b&c=$c&d=$d&e=$e&f=$f&g=d&ignore=.csv")
    obj = urllib2.urlopen(tmpl.substitute(locals()))
    fid = open("%s.csv" % (name,), 'w')
    fid.write(obj.read())
    fid.close()
    obj.close()
    
# Return a date array which can be used with matplotlib's plot_date
def yh_convert_date(arr):
    start = datetime.date(1,1,1)
    return [datetime.date(x,y,z) for x, y, z in zip(arr['year'], arr['month'], arr['day'])]

# Plot stock with date
def plot_stock(arr, field='adj_close', **kwd):
    dates = yh_convert_date(arr)
    plot_date(dates, arr[field], **kwd)
     
gf_regex = r"(\d{1,2})-([A-Za-z]{3})-(\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+)\n"
gf_dtype = [('day', 'i2'), ('month', 'S3'), ('year', 'i4'), ('open', 'f4'), ('high', 'f4'), ('low', 'f4'), ('close', 'f4'), ('volume', 'i4')]

yf_regex = r"(\d{4})-(\d{2})-(\d{2}),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+[.]\d+),(\d+),(\d+[.]\d+)"
yf_dtype = [('year', 'i4'), ('month', 'i2'), ('day', 'i2'), ('open', 'f4'), ('high', 'f4'), ('low', 'f4'), ('close', 'f4'), ('volume', 'i4'), ('adj_close', 'f4')]

names = ['yhoo', 'goog', 'ibm', 'ge', 'msft', 'aapl', 'ebay', 'dell', 'csco', 'siri']
gldict = globals()

def get_stocks():
    global gldict
    for name in names:
        filename = "%s.csv" % name
        if not os.path.exists(filename):
            yh_download(name)
        arr = fromregex(filename, yf_regex, yf_dtype)
        gldict[name] = arr


def get_returns(*args):
    x = []
    for arg in args:
        pass
        





