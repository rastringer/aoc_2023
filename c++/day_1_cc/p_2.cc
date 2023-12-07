#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <charconv>

// Let's split the code into functions vs p_1
std::map<std::string, int> createDigitMap() {
    
    std::map<std::string, int> digitMap;
    digitMap["one"] = 1;
    digitMap["two"] = 2;  
    digitMap["three"] = 3;
    digitMap["four"] = 4;
    digitMap["five"] = 5;  
    digitMap["six"] = 6;
    digitMap["seven"] = 7;
    digitMap["eight"] = 8;
    digitMap["nine"] = 9; 

    return digitMap;
}

// Extract the numberical digits from the strings
std::vector<char> extractDigits(const std::string& line) {
  std::vector<char> digits;
  std::map<std::string, int> digitMap = createDigitMap();
  
  for (char c : line) {
    if (std::isdigit(c)) {
      digits.push_back(c);
    }
    for (const auto& [word, value]: digitMap) {
        if (line.find(word, c) != std::string::npos) {
            digits.push_back(value);
            c += word.length() -1;
        }
    }
  }
  return digits;
}

// Concatenate first, last digits eg 7, 8 = 78
int concatenateDigits(const std::vector<char>& digits) {
  if (digits.empty()) {
    return 0; // No digits, return 0
  }

  int firstDigit = digits[0] - '0';
  int lastDigit = digits.back() - '0';
  
  return (firstDigit * 10) + lastDigit;
}

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
        std::vector<char> digits = extractDigits(l);
        int concat = concatenateDigits(digits);
        total += concat;
    }
    std::cout << total;
  
    return 0;
}
