#!/bin/sh

CFLAGS=`python-config --cflags`
LDFLAGS=`python-config --ldflags`
gcc $CFLAGS -c fact.c -o fact.o
gcc $CFLAGS -c fact_wrap.c -o fact_wrap.o
gcc -dynamiclib $CFLAGS $LDFLAGS fact.o fact_wrap.o -o example.so
