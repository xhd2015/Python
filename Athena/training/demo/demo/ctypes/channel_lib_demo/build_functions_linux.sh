gcc -fPIC -c -Wall functions.c
gcc -shared -o libfunctions.so functions.o
