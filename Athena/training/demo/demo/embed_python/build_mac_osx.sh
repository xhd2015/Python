gcc -arch i386 -I/Library/Frameworks/Python.framework/Versions/Current/include/python2.7  -c -o embed_demo1.o embed_demo1.c
gcc -arch i386 embed_demo1.o /Library/Frameworks/Python.framework/Versions/Current/lib/libpython2.7.dylib -o embed_demo1
