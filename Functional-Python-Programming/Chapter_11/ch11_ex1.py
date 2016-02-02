#!/usr/bin/env python3
"""Functional Python Programming

Chapter 11, Example Set 1
"""
import math

from functools import wraps
def nullable( function ):
    @wraps(function)
    def null_wrapper( arg ):
        return None if arg is None else function(arg)
    return null_wrapper

@nullable
def nlog( x ):
    return math.log(x)

@nullable
def nround4( x ):
    return round(x,4)

test_Null_Log= """
>>> nlog = nullable( math.log )
>>> some_data = [ 10, 100, None, 50, 60 ]
>>> scaled = map( nlog, some_data )
>>> [nround4(v) for v in scaled]
[2.3026, 4.6052, None, 3.912, 4.0943]

"""

nlog = nullable( math.log )
nround4= nullable( lambda x: round(x,4) )

test_Null_Log2= """
>>> some_data = [ 10, 100, None, 50, 60 ]
>>> scaled = map( nlog, some_data )
>>> [nround4(v) for v in scaled]
[2.3026, 4.6052, None, 3.912, 4.0943]
"""

def null2( function ):
    @wraps(function)
    def null_wrapper( *arg, **kw ):
        try:
            return function( *arg, **kw )
        except TypeError as e:
            if 'NoneType' in e.args[0]:
                return None
            raise
    return null_wrapper

test_null2= """
>>> ndivmod= null2( divmod )
>>> ndivmod( None, 2 )
>>> ndivmod( 2, None )
>>> try:
...    ndivmod( "22", "7" )
... except TypeError as e:
...    print(e)
unsupported operand type(s) for divmod(): 'str' and 'str'
"""

import logging, sys
def logged( function ):
    @wraps(function)
    def log_wrapper( *args, **kw ):
        log= logging.getLogger(function.__qualname__)
        try:
            result= function( *args, **kw )
            log.info( "({0!r} {1!r}) => {2!r}".format(args, kw, result) )
        except Exception as e:
            log.exception( "({0!r} {1!r})".format(args, kw) )
            raise e
    return log_wrapper

test_logged_divmod="""
>>> ldivmod= logged(divmod)
>>> logging.basicConfig( stream=sys.stdout, level=logging.INFO )
>>> try: # doctest: +ELLIPSIS
...    ldivmod( 3, None )
... except Exception:
...    pass
ERROR:divmod:((3, None) {})
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for divmod(): 'int' and 'NoneType'
>>> ldivmod( 22, 7 )
INFO:divmod:((22, 7) {}) => (3, 1)
"""

import decimal
def bad_data( function ):
    @wraps(function)
    def wrap_bad_data( text, *args, **kw ):
        try:
            return function( text, *args, **kw )
        except (ValueError, decimal.InvalidOperation):
            cleaned= text.replace(",","")
            return function( cleaned, *args, **kw )
    return wrap_bad_data

test_bad_data="""
>>> from decimal import Decimal
>>> bd_int= bad_data( int )
>>> bd_float= bad_data( float )
>>> bd_decimal= bad_data( Decimal )
>>> bd_int( "13" )
13
>>> bd_int( "1,371" )
1371
>>> bd_int( "1,371", base=16 )
4977
>>> bd_float("17")
17.0
>>> bd_float("1,701")
1701.0
>>> bd_decimal(19)
Decimal('19')
>>> bd_decimal("1,956")
Decimal('1956')
"""

def clean_list( text, char_list ):
    if len(char_list) == 0: return text
    return clean_list( text.replace(char_list[0],""), char_list[1:] )

import decimal
def bad_char_remove( *char_list ):
    def cr_decorator( function ):
        @wraps(function)
        def wrap_char_remove( text, *args, **kw ):
            try:
                return function( text, *args, **kw )
            except (ValueError, decimal.InvalidOperation):
                cleaned= clean_list( text, char_list )
                return function( cleaned, *args, **kw )
        return wrap_char_remove
    return cr_decorator

test_bad_char_remove="""
>>> from decimal import Decimal
>>> @bad_char_remove("$", ",")
... def currency(text, **kw):
...    return Decimal(text, **kw)
>>> currency( "13" )
Decimal('13')
>>> currency( "$3.14" )
Decimal('3.14')
>>> currency( "$1,701.00" )
Decimal('1701.00')
"""

def then_convert( convert_function ):
    def then_convert_decorator( clean_function ):
        @wraps(clean_function)
        def cc_wrapper( text, *args, **kw ):
            try:
                return convert_function( text, *args, **kw )
            except (ValueError, decimal.InvalidOperation):
                cleaned= clean_function( text )
                return convert_function( cleaned, *args, **kw )
        return cc_wrapper
    return then_convert_decorator

test_then_convert_1="""
>>> @then_convert(int)
... def drop_punct(text):
...    return text.replace(",","").replace("$","")
>>> drop_punct("1,701")
1701
>>> drop_punct("97")
97
>>>
"""

test_then_convert_2="""
>>> def drop_punct(text):
...    return text.replace(",","").replace("$","")
>>> drop_punct_int = then_convert(int)(drop_punct)
>>> drop_punct_int("1,701")
1701
>>> drop_punct_int("97")
97
>>>
"""

def normalize( mean, stdev ):
    normalize = lambda x: (x-mean)/stdev
    def concrete_decorator( function ):
        @wraps(function)
        def wrapped( data_arg ):
            z = map( normalize, data_arg )
            return function( z )
        return wrapped
    return concrete_decorator

test_normalize = """
>>> d = [ 2, 4, 4, 4, 5, 5, 7, 9 ]
>>> from Chapter_4.ch04_ex4 import mean, stdev
>>> m_d, s_d =  mean(d), stdev(d)
>>> @normalize(m_d, s_d)
... def norm_list(d):
...    return list(d)
>>> norm_list(d)
[-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]
>>> z = lambda x, m, s: (x-m)/s
>>> list( z( x, mean(d), stdev(d) ) for x in d )
[-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]

>>> @normalize(m_d, s_d)
... def norm_sum(d):
...      return sum(d)
>>> norm_sum(d)
0.0

"""

__test__ = {
    "test_Null_Log": test_Null_Log,
    "test_Null_Log2": test_Null_Log2,
    "test_null2": test_null2,
    "test_logged_divmod": test_logged_divmod,
    "test_bad_data": test_bad_data,
    "test_bad_char_remove": test_bad_char_remove,
    "test_then_convert_1": test_then_convert_1,
    "test_then_convert_2": test_then_convert_2,
    "test_normalize": test_normalize,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    #performace()
