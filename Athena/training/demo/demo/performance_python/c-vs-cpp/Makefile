CFLAGS=-O3 -Wall -arch i386
CXXFLAGS=-O3 -Wall -arch i386

EXES= count-distinct.c.x \
      count-distinct.cpp.x \
	  count-distinct-v1.cpp.x \
	  count-distinct-v2.cpp.x \
	  count-distinct-v3.cpp.x \

all: $(EXES) words.txt

words.txt : /usr/share/dict/words
	python ./make-words.py < /usr/share/dict/words > words.txt

count-distinct.c.x : count-distinct.c
	gcc $(CFLAGS) count-distinct.c -o count-distinct.c.x

count-distinct.cpp.x : count-distinct.c
	g++ $(CXXFLAGS) count-distinct.c -o count-distinct.cpp.x

count-distinct-v1.cpp.x : count-distinct-v1.cpp
	g++ $(CXXFLAGS) count-distinct-v1.cpp -o count-distinct-v1.cpp.x

count-distinct-v2.cpp.x : count-distinct-v2.cpp
	g++ $(CXXFLAGS) count-distinct-v2.cpp -o count-distinct-v2.cpp.x

count-distinct-v3.cpp.x : count-distinct-v3.cpp
	g++ $(CXXFLAGS) count-distinct-v3.cpp -o count-distinct-v3.cpp.x

clean:
	-rm $(EXES) words.txt
