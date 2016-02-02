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

  std::cout << "Words: " << base.distinctcount() << std::endl;
  return 0;
}
