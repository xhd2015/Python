#!/bin/sh

PROGS=( 
./count-distinct.py 
./count-distinct.c.x 
./count-distinct.cpp.x 
./count-distinct-v1.cpp.x 
./count-distinct-v2.cpp.x 
./count-distinct-v3.cpp.x )

for prog in "${PROGS[@]}" ; do
    echo "Program: " $prog
    time $prog < words.txt
done
