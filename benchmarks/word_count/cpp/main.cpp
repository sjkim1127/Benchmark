#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

int main() {
    std::ifstream file("../../data/input.txt");
    if (!file.is_open()) {
        std::cerr << "Failed to open input.txt" << std::endl;
        return 1;
    }

    std::unordered_map<std::string, int> counts;
    std::string word;
    while (file >> word) {
        counts[word]++;
    }

    std::cout << "Unique words: " << counts.size() << std::endl;
    return 0;
}
