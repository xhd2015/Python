http://unthought.net/c++/c_vs_c++.html

-------------------------------------------------------------------------------


C versus C++
by Jakob Østergaard
February 24th, 2004
Introduction
About once a year, the "C versus C++" (and commonly "versus just about any other language imaginable") discussion pops up on the Beowulf mailing list. 2004 turns out to be no exception from this rule.

Someone asked:

hey

        can anybody tell me
what do i choose for programing
either GNU c or JAVA  for implementing some
networkprograms using some linux systemcalls

Being a C++ evangelist (for what I believe are very good reasons), I suggested that the person started his project in C++ instead of Java or C.

Now, the language wars will never end, and everyone who enjoys programming have their own favourite language. I do not believe that I will ever manage to convince the unwashed masses that C++ is a superior language - yet, when someone cries out for advice, as was the case, I will of course give my best recommendations - and since I firmly believe that C++ is a superior general purpose programming language, I am going to recommend it. That was the start of "Beowulf Language War 2004". Q1 I guess ;)
Why C++ is a superior general purpose programming language
There will always be some problems that are better solved in one language than another. There will always be languages that solve specific problems "better" than any other language, for some definition of "better". However, a very very large number of problems have very similar needs (some I/O, some computation) and face similar requirements (reasonable reliability, reasonable performance).
A little history
The C programming language is a very general purpose programming language. It is used to solve problems ranging from operating system kernels, over compilers to graphical user interfaces. C was conceived in the early 1970s by Dennis M. Ritchie. The C programming language was first standardized in the mid 1980s.

The C++ programming language was initially created by Bjarne Stroustrup, as a "better C". C++ was an attempt to extend and (to some extent) change the C programming language to overcome some of the common and big problems with the language. C++ was first standardized in 1998, and as such, is a much younger language than C.
So, what's the deal with C++?
I'm assuming that you know C already. If you do not, then this article really isn't for you.

For the vast majority of problems out there, I state that C++ provides no significant downsides and a number of significant improvements. Bold? Some people seem to think so, but it's really the case. Let's start out by clearing up a few very common C++ misunderstandings:

    C++ is slower than C Wrong! Many C programs are valid C++ programs as well - and such a C program should run at identical speed when translated with either the C and with the C++ compiler.
    C++ specific features give overhead Wrong! The so-called overhead introduced by certain C++ specific features (such as virtual function calls or exceptions), is comparable to the overhead you yourself would introduce should you choose to go thru the pain it would be to implement a similar feature in C.
    C++ is object oriented Wrong! The C++ language contains some language extentions over C, that make object oriented programming and generic programming more convenient. C++ does not force object oriented design anywhere - it merely allows for it if the programmer deems OO feasible. C allows for object oriented programming as well, C++ only makes it simpler and less error prone. 

So, if you believe me, we have established that "C++ is not significantly worse than C". Let's have a look at what it is that makes C++ a better C:

    Stronger typing The type system in C++ is stronger than in C. This prevents many common programming errors - coupled with the next very important feature, the stronger type system even manages not to be an inconvenience.
    Parameterized types The template keyword allows the programmer to write generic (type-agnostic) implementations of algorithms. Where in C, one could write a generic list implementation with an element like:

    struct element_t {
       struct element_t *next, *prev;
       void *element;
    };

    C++ allows one to write something like:

    template <typename T>
    struct element_t {
       element_t<T> *next, *prev;
       T element;
    };

    Not only does the C++ implementation prevent common programming errors (like putting an element of the wrong type on the list), it also allows better optimization by the compiler! For example, a generic sort implementation is available in both C and C++ - the C routine is defined as:

    void qsort(void *base, size_t nmemb, size_t size,
               int(*compar)(const void *, const void *));

    whereas the C++ routine is defined as

    template 
    void sort(RandomAccessIterator first, RandomAccessIterator last);

    The difference being, that for example sorting an array of integers, would, in the C case, require a function call for every single compare, whereas the C++ implementation would allow the compiler to inline the integer comparison calls, as the actual sort routine is instantiated at compile time, automatically by the compiler, with the correct types inserted in the template arguments.
    A bigger standard library C++ allows the full use of the C standard library. This is very important of course, as the C standard library is an invaluable resource when writing real world programs. However, C++ includes the Standard Template Library. The STL contains a number of useful templates, like the sort routine above. It includes useful common data structures such as lists, maps, sets, etc. Like the sort routine, the other STL routines and data structures are "tailored" to the specific needs the programmer has - all the programmer has to do is fill in the types. Of course, the STL is no silver bullet - but it does provide a great help very often, when solving general problems. How often have you implemented a list in C? How often would an RB-tree have been a better solution, if only you had had the time to do it? With the STL you do not need to make such compromises - use the tree if it's a better fit, it's as easy as using the list. 

Ok, so I've been telling about all the good parts. Are there no downsides? Of course there is. Howver, they are shrinking day by day. Let me explain:

    There are no good C++ compilers It's been like this for a long time. But you must remember, that the language was standardized in 1998 - it is a complex language, more complex than C. It has taken a long time for compilers to catch up to the standard. But as of this writing, there are good compilers available for the most widely used platforms out there; GCC in versions 3.X are generally very good, and it runs on GNU/Linux and most UNIX platforms. Intel has a good compiler for Win32 - it is also pretty good, but unfortunately it still relies on the MS STL which is sub-par.
    People don't know good C++ This is not an often heard complaint, but it's something that I see a lot. C++ is a big and complex language - but it also used to be a language that was hyped a lot, especially back in the "OOP solves hunger, cures AIDS and cancer" days. The result seems to be that a lot of really poor C++ code, basically bad C with a few class statements here and there, is out there and is being used as learning material. This means, a lot of people who believe they know C++ actually write really crap code. That's too bad, and it's a problem, but I think it's unfair to blame C++ for this. 

So, the only two major problems with C++ are results of C++ being a young language. In time they will vanish. And for most problems out there, if you can get good programmers (or learn good C++ yourself), the problems are not really an issue today.

Note, that I am not arguing that everything is rewritten in C++. There are many large projects out there which are written in C - I do not believe that it is a good idea to just "convert" them to C++. C++ allows for cleaner solutions than C does, for a great many problems. Doing a minimal conversion of a solution which is "as clean as it gets" in C, to C++, would convert "good C" code into "poor C++". That is not a change to the better!

I have converted code from C to C++. But such a conversion has always ended up being a complete rewrite. From scratch. A redesign as such may not be necessary - after all, C++ does not force any new design principles down your throat, and if the original C code was well designed, there may not be a need to redo that.

However, for new projects starting out today, I fail to see why anyone (who knows C++ or is willing to learn it) would use C rather than C++. Unless, of course, that one of the two problems stated earlier are important.
The Challenge
So, after a little back and forth on the Beowulf mailing list, where various people (myself included) argued for the pros and cons of their pet languages and other peoples (inferior of course) pet languages, I decided to put out a challenge; I presented a problem, and a small and clean solution for it, and challenged the list to come up with a better solution.

The problem: Write a program that reads text from standard-input, and returns (prints) the total number of distinct words found in the text.

In short, I presented a C++ solution to the problem, and challenged someone to do it in C. I even wrote:

I still guarantee you two things:
1) Your code will be longer
2) Your program will be slower

Hey, you gotta be bold to keep these things interesting!
Initial solutions
The small C++ solution
The following is the solution I presented with my challenge. It is a total of 15 lines of C++. It uses the STL std::set template with an std::string as the template argument, to hold the words read from stdin. In non-C++ speak this means I use an RB-tree of strings.

#include <set>
#include <string>
#include <iostream>

int main(int argc, char **argv)
{       
        // Declare and Initialize some variables
        std::string word;
        std::set<std::string> wordcount;
        // Read words and insert in rb-tree
        while (std::cin >> word) wordcount.insert(word);
        // Print the result
        std::cout << "Words: " << wordcount.size() << std::endl;
        return 0;
}

Personally, I think this is elegant. Anyone who knows C++ will be able to glance at the code and understand completely what it does, within a few tens of seconds. The code is short, and only extremely simple well-understood operations are performed on the data - it is quickly established that the code is correct. If the beholder understands the language, of course, but this is a problem with all languages.
The faster C solution
Of course, shortly after that post, someone replied with a faster implementation in C. I should have known that. I was happy to see, that the C implementation was indeed longer - this faster solution is 85 lines long.

Note, the actual code presented here is not the exact suggestion sent to the list - I changed the printing of the result at the bottom of the code, so that the program prints out the number of distinct words - the original code was made to print out an unsorted list of word frequencies. This change only touches a few of the very last lines in the code, it touches nothing in the central parts of the program at all.

Unlike my initial solution, this program uses a hash to store the distinct words. A hash can be faster than an RB-tree - a well dimensioned hash can exhibit O(1) complexity for insertions where an RB-tree exhibits O(log(n)) complexity.

The change of algorithm is unfortunate for a language-performance comparison point of view - as the C implementation will exhibit different run-time performance than the C++ implementation, for reasons that are not related to the choice of language at all. However, I'm not going to bitch about it, I'm going to evaluate the suggestion and still prove my point; that C++ is a better language for solving general purpose programming problems.

Let's have a look at the C code shall we;

/* Copyright (C) 1999 Lucent Technologies */
/* From 'Programming Pearls' by Jon Bentley */

/* wordfreq.c -- list of words in file, with counts */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node *nodeptr;
typedef struct node {
    char *word;
    int count;
    nodeptr next;
} node;

#define NHASH 29989
#define MULT 31
nodeptr bin[NHASH];

unsigned int hash(char *p)
{   unsigned int h = 0;
    for ( ; *p; p++)
        h = MULT * h + *p;
    return h % NHASH;
}

#define NODEGROUP 1000
int nodesleft = 0;
nodeptr freenode;

nodeptr nmalloc()
{   if (nodesleft == 0) {
        freenode = malloc(NODEGROUP*sizeof(node));
        nodesleft = NODEGROUP;
    }
    nodesleft--;
    return freenode++;
}

#define CHARGROUP 10000
int charsleft = 0;
char *freechar;

char *smalloc(int n)
{   if (charsleft < n) {
        freechar = malloc(n+CHARGROUP);
        charsleft = n+CHARGROUP;
    }
    charsleft -= n;
    freechar += n;
    return freechar - n;
}

void incword(char *s)
{   nodeptr p;
    int h = hash(s);
    for (p = bin[h]; p != NULL; p = p->next)
        if (strcmp(s, p->word) == 0) {
            (p->count)++;
            return;
        }
    p = nmalloc();
    p->count = 1;
    p->word = smalloc(strlen(s)+1);
    strcpy(p->word, s);
    p->next = bin[h];
    bin[h] = p;
}

int main()
{   int i;
    nodeptr p;
    char buf[16384];
        unsigned total = 0;
    for (i = 0; i < NHASH; i++)
        bin[i] = NULL;
    while (scanf("%s", buf) != EOF)
        incword(buf);
    for (i = 0; i < NHASH; i++)
        for (p = bin[i]; p != NULL; p = p->next)
            total += p->count ? 1 : 0;
    printf("Words: %d\n", total);
    return 0;
}

Well there you have it. An interesting exchange happened on the list after this was posted:

> As in maybe it's just me, but when I look at Jakob's code I have no idea
> how it works.  What are these routines?  What do they do?  Where's the
> logic?  Oh, I can read the comments and see the keywords and sort of
> guess that all sorts of dark magic is being done; I just have no idea
> how it does it, any more than I would if one took Jakob's code or my
> code or anybody's code for the same task and wrapped it up in a single
> routine:

And here I argue that this is where C++'s strength becomes evident. STL is
_standard_ (hence its name). Thus, for a C++ programmer, Jakob's code is
comprehensible in one 15second long glimpse and this programmer can
immediately use (trust?) the code. With the equivalent C code from the posted
link, I personally have the problem that I need at least 15 minutes to read
and understand it, and even then, I can't be sure I identified all gotchas
and thus I can use it without major crashes and problems. I argue that the
biggest problem with C up until glib and gsl (thus very recently) was exactly
the lack of high level routines collected in a ubiquous library.

Showdown, so far
For benchmarking, I use a text file containing mainly ASCII english text. The file is 55704078 bytes in size and contains 6727317 words in total. It holds 576059 distinct words.

C and C++ code was compiled with GCC 3.3.2, using the following switches:

 -O3 -Wall -g -march=pentium2

Only -O3 -march=pentium2 have performance impacts - basically they enable all optimization in the compiler, and tells the compiler to generate code for an Intel PentiumII processor. I run the tests on a PentiumII Celeron machine.

Run-time performance
Solution    Lines of code   Run-time
C++ RB-tree     15  235 sec.
C Hash  85  36 sec.

Wow! Quite a difference! At 567% the code-size, the C implementation gets the work done in 15% of the time of the C++ solution. Quite a difference, in run-time as well as implementation-time.

But this benchmark is no good for the purpose of the "C versus C++" argument - it's two completely different approaces that yield completely different results, for reasons that have nothing to do with the languages used.
Identical algorithms, different languages
What we really need, is to see what C++ can do for the C solution presented. If C++ can make the code

    Shorter (so that it is easier audited/comprehended)
    Generic (so that it can be reused)
    Faster
    Prettier
    brew coffee 

then I believe that I would have a good case for my "C++ is the better C" crusade.

With the time that I spent on this, I was not able to achieve all of those goals. It was a tradeoff between code length/clarity and speed, basically.

As it turned out, making the code more generic did not affect run-time performance, and did not significantly affect code size.

The main thing that affected code size, was, that I made the code reliable and reusable - I changed the C implementation which used global variables and #defines (thus making the implementation unusable if for example someone wanted to use two different hashes in a program), into a generic template class.

A short table summarizing the changes:
C versus C++, hash implementation
Quality     C implementation    C++ implementation
Generality  Hash parameters are defines, everything-global  Hash parameters specified as template parameters, nothing-global
Usability   No memory cleanup - customized allocation routines make addition of cleanup slightly complicated    Full cleanup in hash destructor
The resulting C++ implementation is 121 lines long - that's 36 lines longer than the original C implementation, but the added lines are simply due to the added memory cleanup functionality.

One of the nifty features of the C++ implementation is, that the hash parameters are specified at hash instantiation, as template parameters. So, a program needing two different hashes with different size parameters, would simply declare them as:

my_hash_t<> one;     // Uses default parameters
my_hash_t<11,3> two; // NHASH=11, MULT=3 in this instantiation

While it would of course be possible to adapt the C implementation so that one could use more than one hash in a given program, it would be rather more difficult to adapt the code to actually accept different hash parameters. In fact, for a solution that would be run-time performance comparable to the C++ implementation presented here, one would have to make all routines using the NHASH, MULT, NODEGROUP and CHARGROUP defines (which are template parameters in the C++ implementation) macros!. Now macros ain't pretty - but an entire hash implementation in macros, that's, well, not pretty.
C++'ification of the C solution

/*
 * Rewrite in C++ by Jakob Oestergaard 
 * of:  (original copyright follows)
 */

/* Copyright (C) 1999 Lucent Technologies */
/* From 'Programming Pearls' by Jon Bentley */

/* wordfreq.c -- list of words in file, with counts */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

struct node_t {
  char *word;
  int count;
  node_t *next;
};

template <typename T>
struct alist_t {
  alist_t(size_t elms) : next(0) {
    area = new T[elms];
  }
  ~alist_t() {
    if (next) delete next;
    delete[] area;
  }
  T* allocate(size_t elms) {
    alist_t *n = new alist_t<T>(elms);
    n->next = next;
    next = n;
    return n->area;
  }
  T *area;
  alist_t<T> *next;
};

template <unsigned NHASH = 29989,    unsigned MULT = 31,
      unsigned NODEGROUP = 1000, unsigned CHARGROUP = 1000>
class my_hash_t {
public:
  my_hash_t()
    : bin(NHASH,0), nodesleft(0), charsleft(0),
      nglist(NODEGROUP), cglist(CHARGROUP) { }

  unsigned hash(const char *p) const
  {
    unsigned int h = 0;
    while (*p)
      h = MULT * h + *p++;
    return h % NHASH;
  }

  void incword(const char *s)
  {
    node_t* p;
    int h = hash(s);
    for (p = bin[h]; p; p = p->next)
      if (strcmp(s, p->word) == 0) {
    ++p->count;
    return;
      }
    p = nmalloc();
    p->count = 1;
    p->word = smalloc(strlen(s)+1);
    strcpy(p->word, s);
    p->next = bin[h];
    bin[h] = p;
  }

  node_t *const * begin() const { return &bin[0]; }
  node_t *const * end() const { return &bin[NHASH]; }

private:
  std::vector<node_t*> bin;
  int nodesleft;
  node_t* freenode;
  int charsleft;
  char *freechar;
  alist_t<node_t> nglist;
  alist_t<char> cglist;

  node_t* nmalloc()
  {
    if (nodesleft == 0) {
      freenode = nglist.allocate(NODEGROUP);
      nodesleft = NODEGROUP;
    }
    nodesleft--;
    return freenode++;
  }

  char *smalloc(int n)
  {
    if (charsleft < n) {
      freechar = cglist.allocate(n+CHARGROUP);
      charsleft = n+CHARGROUP;
    }
    charsleft -= n;
    freechar += n;
    return freechar - n;
  }
};

int main()
{
  my_hash_t<> my_hash;
  char buf[16384];
  while (scanf("%s", buf) != EOF)
    my_hash.incword(buf);

  unsigned total = 0;
  for (node_t*const* p = my_hash.begin(); p != my_hash.end(); ++p)
    for (const node_t *e = *p; e; e = e->next)
      total += e->count ? 1 : 0;
  printf("Words: %d\n", total);
  return 0;
}

As you can see, in order to duplicate malloc tricks from the C implementation in a clean manner (which also gives us trivial memory cleanup), I implemented the alist_t template structure - this is an allocation helper which will allocate a number of elements (of some given type), and allows for very efficient expansion of the allocated area (while maintaining the trivial-cleanup property). This accounts for 20 lines of code - the remaining 15 lines of code goes to some extra blank lines, the extra comments in the beginning of the file, and the template class wrapping of the hash implementation.

Now, what you may not realize if you're an old-school C programmer is, that you can actually stick the entire hash implementation - everything in the above listing except for the main routine - in a header file. Yep, that's right - C++ will handle this, the linker will not barf. You can then include this header file in every project you do, where you may need a hash implementation. You define the properties of the has when you instantiate the hash - in your own code. The header file just provides the template implementation. C'mon, that's clever!
Showdown; identical algorithm, C versus C++
So, I set out to provide a solution which was shorter, more generic, faster, prettier etc. During the rewrite of the hash implementation, I needed to decide where to put my focus. The most important properties were, I deemed;

    Speed - the C++ implementation must run as fast or faster than the C implementation
    Generality - the C++ implementation must be easily reusable in other projects (unlike the C implementation)
    Usability - the C++ implementation must manage its memory properly (unlike the C implementation) 

For this, I sacrificed;

    Code length - The C++ implementation is 36 lines longer than the C implementation - I accepted this, as the new code can in fact be used as a component in other projects (unlike the C implementation) 

The actual performance of the two solutions, follows:
Run-time performance
Solution    Lines of code   Run-time
C++ Hash    121     34.697 sec.
C Hash  85  35.929 sec.
The run-times are averages over 10 runs each. Since the algorithms are identical, I actually expected the run-times to be almost equal. The 3% difference in C++'s favour was a surprise - it was a consistent, although small win over all the runs. My best guess as to what causes C++ to be faster is the type system; the compiler can do better optimizations based on aliasing analysis of the variables, due to the stricter type system. But this is just a guess - I did not dig into the assembly code to actually find the reasons behind this.
Conclusion so far
Using identical algorithms, two solutions for the initial challenge are presented - they have similar run-time performance, although C++ does have a small edge. Clearly, this small win would not be the reason alone for chosing languages.

I believe that I have demonstrated how C++ constructs (the template) allows for generic re-usable and flexible implementations without run-time performance overhead, and (the constructor/destructor) allows for automatic initialization and cleanup of data structures - making it simpler for the user of generic data structures, such as the hash presented, to write real-world programs that are reliable and do not leak memory.

I also believe that I have proven, that C++ does not force any particular type of design down anyone's throat. For example, the node_t in my code is almost identical to the struct node in the original C code - there simply was no need to change it, and therefore it was left basically the way that it was.
Further solutions
This is really not directly within the scope of the "C versus C++" challenge, but since my first solution got beaten so severely by the C contender, I did feel that I had to look into why and how this could be.

The reasons for the beating turned out to be pretty interesting.
Fixed C++ solution
C++ provides a very convenient way of dealing with strings. Instead of using the char*, managing your own memory, hoping to get the string lengths right, etc. etc. C++ provides the std::string. This is a really neat little template, wich provides the user with a safe way of dealing with strings. For example:

std::string a = "abc"; // easy initialization from C strings
const char *b = a.c_str(); // easy to get a C string out again
std::string b = "foo" + a; // operations on strings are easy too!
size_t b_len = b.size();   // O(1) behavior for some operations
bool a_eq_b = a == b;      // string comparison, done right

The std::string maintains the length of the string internally - this has several advantages: it is possible to have a string that contains '\0' characters anywhere - '\0' is not special, and of course retrieving the length of a string is fast.

I discovered that for string comparisons (which is the number-one CPU consuming operation in both the C hash implementation and the C++ RB-tree implementation) in my STL use the memcmp routine, whereas the C implementation directly calls the strcmp routine. Now, for some odd reason, the strcmp routine on my system is heavily optimized for the Pentium II processor, while the memcmp routine used when I specify Pentium II optimizations is optimized for the i486 processor. This was one cause for the slowdown - my RB-tree implementation simply could not compare strings as fast as the C implementation, even though it ought to be faster at comparing since it already has O(1) access to the string lengths.

But this was not the whole explanation. It turns out, that using std::cin >> buf is just horribly inefficient. I did not dig further into this to discover why - I guess that all in all, maintaining the length of the string explicitly as the STL std::string does, is just not a win in this scenario. Further, I guess that std::cin is just not horribly well optimized, in the STL that I use. I guess this is understandable - the STL is big, and I/O may just not have been the number one priority for the STL people - understandable, I guess, since the standard C library offers fine routines for doing I/O, and especially when high-performance I/O is a concern, one will use the "raw" read and write system calls anyway.

So, I cooked up a very simple implementation that still uses std::string (because it gives us safe memory management and fully automatic cleanup), but takes the C approach to reading in data from the text file. The code is presented below:

#include <set>
#include <string>
#include <iostream>
#include <stdio.h>

int main(int argc, char **argv)
{       
  // Declare and Initialize some variables
  char buf[16384];
  std::set<std::string> wordcount;
  // Read words and insert in rb-tree
  while (scanf("%s", buf) != EOF) wordcount.insert(buf);
  // Print the result
  std::cout << "Words: " << wordcount.size() << std::endl;
  return 0;
}

The run-time performance of this code ("C++ RB-tree (II)") is presented along with the other measurements in the table below.
Run-time performance
Solution    Lines of code   Run-time
C++ RB-tree (I)     15  235 sec.
C++ Hash    121     34.697 sec.
C Hash  85  35.929 sec.
C++ RB-tree (II)    15  63.970 sec.
A litle change with a great effect. Too bad the STL that I use isn't up to par with the C library yet - the mark-I code was prettier I think, but at least this code is a very short example that in 178% of the time but only 18% of the code does what the C program does.
Faster C++ solution
Well, someone else started, not me! Different algorithms I mean. I present here a solution which is faster than the C implementation, uses a completely different algorithm, and is written in C++ only.

It really serves no purpose. Except perhaps to boost my ego by presenting something that is faster than the "programming pearl" presented earlier ;)

The following solution uses something that is almost-but-not-quite a digital trie. In my tests, it uses about four times as much memory as the hash implementations did. It sacrifices memory footprint for performance.

#include <unistd.h>
#include <vector>
#include <cctype>
#include <stdint.h>
#include <iostream>

const size_t pagesize = 4096;

struct knot_t {
  knot_t() : exists(false), childcount(0), children(0) {  }
  knot_t* child(unsigned c) {
    // Look for a matching child
    if (children) {
      unsigned i = childcount / 2;
      unsigned leftpos = 0;
      unsigned rightpos = childcount;
      while (children[i].letter != uint8_t(c)) {
    if (uint8_t(c) < children[i].letter) {
      rightpos = i;
      i = (leftpos + i) / 2;
    } else {
      leftpos = i+1;
      i = (rightpos + i) / 2;
    }
    if (rightpos == leftpos)
      goto nomatch;
      }
      return children + i;
    }
  nomatch:
    // Create matching child - insert in order
    knot_t *nary = new knot_t[childcount + 1];
    knot_t *destp = nary;
    knot_t *sourcep = children;
    knot_t *endsource = children + childcount;
    while (sourcep != endsource && sourcep->letter < c)
      *destp++ = *sourcep++;
    knot_t *outp = destp++;
    while (sourcep != endsource)
      *destp++ = *sourcep++;

    delete[] children;
    children = nary;
    outp->letter = c;
    childcount++;
    return outp;
  }
  unsigned distinctcount() const {
    unsigned total = exists ? 1 : 0;
    for (unsigned i = 0; i != childcount; ++i)
      total += children[i].distinctcount();
    return total;
  }
  bool exists;
private:
  uint8_t letter;
  unsigned short childcount;
  knot_t *children;
};


int main(int argc, char **argv)
{
  knot_t base;
  char buffer[pagesize];
  knot_t *curnot = 0;

  while (ssize_t r = read(0, buffer, pagesize)) {
    if (r <= 0)
      break;
    for (unsigned bufpos = 0; bufpos != unsigned(r); ++bufpos) {
      uint8_t c = buffer[bufpos];
      if (isspace(c)) {
    if (!curnot)
      continue;
    curnot->exists = true;
    curnot = 0;
    continue;
      }
      if (!curnot) {
    curnot = base.child(c);
    continue;
      }
      curnot = curnot->child(c);
    }
  }
  if (curnot)
    curnot->exists = true;

  std::cout << "Distinct: " << base.distinctcount() << std::endl;
  return 0;
}

Run-time performance
Solution    Lines of code   Run-time
C++ RB-tree (I)     15  235 sec.
C++ Hash    121     34.697 sec.
C Hash  85  35.929 sec.
C++ RB-tree (II)    15  63.970 sec.
C++ Ego-booster     93  18.108 sec.
So there you have it.

Of course, the ego-booster could also be implemented in C. Probably with negligible run-time penalty (as per the previous tests). This code really uses virtually none of the niceties that C++ provides, in mainly serves to prove that C++ can be used for real performance critical code, where old-timers would cry "C" if asked. Well, I'm not asking, I was too busy coding ;)

The above code spends about half of the run-time waiting for a register stall, because I store the letter as a uint8_t instead of an unsigned. It would be simple to change, but it would cost about 30% extra on the memory footprint. Ah, tradeoffs...
The end
So, that's it for now. If you have feedback or questions, just let me know. 
