#!/usr/bin/python3
# bwCGI.py by Bill Weinman <http://bw.org/contact/>
# Copyright (c) 1995-2010 The BearHeart Group, LLC
#

from cgi import FieldStorage
import cgitb
import os

__version__  = '0.3.2'
_cookie_var = 'HTTP_COOKIE'

class bwCGI:
    ''' handy cgi stuff '''
    _header_state = False            # True after header has been sent
    cgi_cookies = dict()
    cgi_headers = dict()

    def __init__(self, **kwargs):
        self.set_header('Content-type', kwargs.get('content_type', 'text/html'))
        if _cookie_var in os.environ:
            self.parse_cookies()

    def set_header(self, k, v):
        '''
            set a header
            use str for single value, list for multiples values
        '''
        if k in self.cgi_headers:
            if isinstance(self.cgi_headers[k], list): self.cgi_headers[k].append(v)
            else: self.cgi_headers[k] = [ self.cgi_headers[k], v ]
        else:
            self.cgi_headers[k] = str(v)
        return v

    def get_header(self, k):
        return self.cgi_headers.get(k, None)

    def send_header(self):
        ''' send the header(s), only once '''
        if self._header_state: return
        for k in self.cgi_headers:
            value = self.cgi_headers[k]
            if isinstance(value, list):
                for v in value: print('{}: {}'.format(k, v))
            else:
                print('{}: {}'.format(k, value))
        print()
        self._header_state = True
        cgitb.enable()  # only after the header has been sent

    def set_cookie(self, key, value, **kwargs):
        ''' kwargs can include expires, path, or domain
        '''
        cookie = '{}={}'.format(str(key), str(value))
        if kwargs.keys():
            for k in kwargs.keys():
                cookie = '{}; {}={}'.format(cookie, k, kwargs[k])
        self.set_header('Set-Cookie', cookie)

    def parse_cookies(self):
        for ck in os.environ[_cookie_var].split(';'):
            lhs, rhs = ck.strip().split('=')
            self.cgi_cookies[lhs.strip()] = rhs.strip()

    def get_cookies(self):
        return self.cgi_cookies;

    def get_cookie(self, key):
        return self.cgi_cookies.get(key, None)

    def linkback(self):
        ''' return a relative URI for use as a linkback to this script '''
        for e in ( 'REQUEST_URI', 'SCRIPT_NAME' ):
            if e in os.environ:
                l = os.environ[e]
                break
        else: return '*** cannot make linkback ***'
        if '?' in l: l = l[0:l.find('?')]
        return os.path.basename(l)

    def vars(self):
        return FieldStorage()

    # utility methods

    def entity_encode(self, s):
        ''' convert unicode to XML entities
            returns encoded string
        '''
        outbytes = bytearray()
        for c in s:
            if ord(c) > 127:
                outbytes += bytes('&#{:d};'.format(ord(c)), encoding = 'utf_8')
            else: outbytes.append(ord(c))
        return str(outbytes, encoding = 'utf_8')

def test():
    if _cookie_var not in os.environ:
        os.environ[_cookie_var] = 'one=1; two=2; three=3'
    cgi = bwCGI(content_type='text/plain')
    cgi.set_header('X-bwCGI', __version__)
    cgi.set_header('X-number', 42)
    cgi.set_cookie('one', 1)
    cgi.set_cookie('two', 2)
    cgi.set_cookie('three', 3, path='/', expires='31-Dec-2010 23:59:59 GMT', domain='.bw.org')
    cgi.set_cookie('five', 5)
    cgi.send_header()     # should only see one set of headers
    cgi.send_header()
    cgi.send_header()
    print('Hello, CGI')
    print('header X-bwCGI:', cgi.get_header('X-bwCGI'))
    print('header Eggs:', cgi.get_header('Eggs'))
    print('Cookies:')
    print(sorted(cgi.get_cookies()))
    print('cookie one:', cgi.get_cookie('one'))
    print('cookie seven:', cgi.get_cookie('seven'))

if __name__ == '__main__': test()

