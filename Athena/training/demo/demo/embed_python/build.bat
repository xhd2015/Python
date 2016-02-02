gcc -c -Ic:\Python27\include embed_demo1.c
gcc embed_demo1.o -lpython27 -Lc:\Python27\libs -o embed_demo1
