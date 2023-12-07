#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <typeinfo>

int main() {
    std::ifstream infile("input.txt");
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(infile, line)) {
        lines.push_back(line); 
    }
    infile.close();

    int total = 0;

    // lines vector now contains the file content  
    for(auto &l : lines) {
        // Vector to hold the digits, chars for now
        std::vector<char> digits;
        for(char c : l) {
            if(std::isdigit(c)) {
                digits.push_back(c);
            }
        }
        
        int first = digits[0] - '0'; // Convert char to int
        int last = digits.back() - '0'; // Convert char to int
        int concat = (first * 10) + last; 

        total += concat;
    }

    std::cout << total;
  
    return 0;
}