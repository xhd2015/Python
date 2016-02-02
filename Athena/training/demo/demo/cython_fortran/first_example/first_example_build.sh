#!/bin/sh

gfortran -std=f2003 -pedantic -c first_example.f90
gcc -c first_example_main.c
gcc first_example_main.o first_example.o -o first_example_main
