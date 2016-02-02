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
