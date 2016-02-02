gcc -c -I. -Ic:\Python27\include fact.c fact_wrap.c
gcc -shared fact.o fact_wrap.o -Lc:\python27\libs -lpython27 -o example.pyd
