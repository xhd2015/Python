gcc -c -I. -Ic:\Python27\include nan2zero.c
gcc -c -I. -Ic:\Python27\include -Ic:\Python27\lib\site-packages\numpy\core\include nan2zero_wrap.c
gcc -shared nan2zero.o nan2zero_wrap.o -Lc:\python27\libs -lpython27 -o nan2zero.pyd
