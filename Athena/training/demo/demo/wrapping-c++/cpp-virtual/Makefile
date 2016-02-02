
all:
	python setup.py build_ext --inplace

cpp:
	g++ -c cpp_virt.cxx
	g++ -c main.cpp
	g++ cpp_virt.o main.o -o cpp_virt.x

clean:
	rm -rf build *.so *.o *_wrap* cpp_virt.py* *.pyc cpp_virt.x
