gcc -c -arch i386 nan2zero.c -o nan2zero.o
gcc -c -arch i386 nan2zero_wrap.c -I/Library/Frameworks/Python.framework/Versions/Current/lib/python2.7/site-packages/numpy/core/include -I/Library/Frameworks/Python.framework/Versions/Current/include/python2.7 -o nan2zero_wrap.o
gcc -dynamiclib -arch i386 nan2zero.o nan2zero_wrap.o -L/Library/Frameworks/Python.framework/Versions/Current/lib -lpython2.7 -o nan2zero.so
