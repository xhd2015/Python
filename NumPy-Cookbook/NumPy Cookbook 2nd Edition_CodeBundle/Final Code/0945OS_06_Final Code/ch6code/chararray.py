import urllib2
import numpy as np
import re

response = urllib2.urlopen('http://python.org/')
html = response.read()
html = re.sub(r'<.*?>', '', html)
carray = np.array(html).view(np.chararray)
carray = carray.expandtabs(1)
carray = carray.splitlines()
print(carray)


