#!/usr/bin/python3
# bwTL - BW's template library
# by Bill Weinman [http://bw.org/]
# Copyright 1995-2010 The BearHeart Group LLC

import re
import sys

__version__ = '0.6.1'
utf_8 = 'utf_8'

class tlStr:
    ''' string templating class '''
    __vars = {}
    _sep = '\$'
    flags = dict(
        showUnknowns = False,
        entityEncode = True
    )

    def __init__(self, s = '', **kwargs):
        self.__s = s
        self._init_re(kwargs)

    def _init_re(self, kwargs):
        if 'sep' in kwargs: self._sep = kwargs['sep']
        self.__re = re.compile(r'{0}(.*?){0}'.format(self._sep))

    def _init_flags(self, kwargs):
        self.flags['showUnknowns'] = kwargs.get('showUnknowns', False)
        self.flags['entityEncode'] = kwargs.get('entityEncode', True)

    def var(self, k, v = None):
        if v is not None:
            self.__vars[k] = str(v)
        if k in self.__vars:
            return self.__vars[k]
        elif self.flags['showUnknowns']:
            return '** UNK {} **'.format(k)
        else:
            return None

    def parse(self, str = None):
        s = self.__s if str is None else str
        s = re.sub(self.__re, self.replace, s)
        return s

    def replace(self, s):
        return self.var(s.group(1))

class tlFile(tlStr):
    ''' file templating '''
    def __init__(self, fn, **kwargs):
        self.__fh = open(fn, 'r', encoding = utf_8) if fn else None
        self._init_flags(kwargs)
        self._init_re(kwargs)

    def reset(self):
        self.__fh.seek(0)

    def file(self, fn):
        self.__fh = open(fn, 'r', encoding = utf_8)

    def readline(self, **kwargs):
        l = self.__fh.readline()
        return self.parse(l)

    def readlines(self, **kwargs):
        for l in self.__fh.readlines():
            yield self.parse(l)

def bwtl_test():
    print('bwTL.py version', __version__)
    x = 'This has a variable ($var$) and another (@two@) in it'

    st = tlStr(x, sep='@')
    print('x is:', x)
    st.var('var', 'ONE')
    st.var('two', 'TWO')
    print(st.parse())

    fn = 'templatefile.txt'
    try:
        ft = tlFile(fn)
        ft.var('one', 'spam')
        ft.var('two', 'eggs')
        ft.var('three', 'ham')
        ft.var('four', 'rubber chicken')
        ft.var('five', '55555')
    
        print(str("ft.readline: " + ft.readline()).strip())
        
        for l in ft.readlines():
            print(l.strip())

        print('five is [{}]'.format(ft.var('five')))

    except IOError as e:
        print("Cannot open template file: {}".format(e))

if __name__ == "__main__": bwtl_test()

