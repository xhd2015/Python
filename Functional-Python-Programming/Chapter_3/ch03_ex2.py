#!/usr/bin/env python3
"""Functional Python Programming

Chapter 3, Example Set 2
"""

from decimal import *
def clean_decimal_1(text):
    """
    Remove $ and , from a string, return a Decimal.
    
    >>> clean_decimal_1( "$1,234.56" ) 
    Decimal('1234.56')
    """
    if text is None: return text
    try:
        return Decimal(text.replace("$","").replace(",",""))
    except InvalidOperation:
        return text

def replace(str, a, b):
    """Prefix function for str.replace(a,b)."""
    return str.replace(a,b)

def clean_decimal_2(text):
    """
    Remove $ and , from a string, return a Decimal.

    >>> clean_decimal_2( "$1,234.56" ) 
    Decimal('1234.56')
    """
    if text is None: return text
    try:
        return Decimal(replace(replace(text, "$", ""), ",", ""))
    except InvalidOperation:
        return text

def remove( str, chars ):
    """Remove all of the given chars from a string."""
    if chars: return remove( str.replace(chars[0], ""), chars[1:] )
    return str

def clean_decimal_3(text):
    """
    Remove $ and , from a string, return a Decimal.

    >>> clean_decimal_3( "$1,234.56" ) 
    Decimal('1234.56')
    """
    if text is None: return text
    try:
        return Decimal(remove( text, "$,") )
    except InvalidOperation:
        return text

def test():
    import doctest
    doctest.testmod(verbose=2)
    
if __name__ == "__main__":
    test()
