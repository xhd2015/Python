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
