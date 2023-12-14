#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <numeric>

std::set<std::pair<int, int> > get_adj_coords(const std::vector<std::string>& grid) {
    std::set<std::pair<int, int> > coords;

    for (int row_coords = 0; row_coords < grid.size(); ++row_coords) {
        for (int col_coords = 0; col_coords < grid[row_coords].size(); ++col_coords) {
            char current_char = grid[row_coords][col_coords];
            if (isdigit(current_char) || current_char == '.') {
                continue;
            }

            for (int current_row = row_coords - 1; current_row <= row_coords + 1; ++current_row) {
                for (int current_col = col_coords - 1; current_col <= col_coords + 1; ++current_col) {
                    if (current_row >= 0 && current_row < grid.size() &&
                        current_col >= 0 && current_col < grid[current_row].size() &&
                        isdigit(grid[current_row][current_col])) {
                        coords.insert(std::make_pair(current_row, current_col));
                    }
                }
            }
        }
    }

    return coords;
}

std::vector<int> get_adj_nums(const std::set<std::pair<int, int> >& coords, const std::vector<std::string>& grid) {
    std::vector<int> nums;

    for (const auto& coord : coords) {
        int row_coords = coord.first;
        int col_coords = coord.second;
        std::string start;

        while (col_coords < grid[row_coords].size() && isdigit(grid[row_coords][col_coords])) {
            start += grid[row_coords][col_coords];
            ++col_coords;
        }

        nums.push_back(std::stoi(start));
    }

    return nums;
}

int main() {
    std::ifstream file("input.txt");
    if (!file.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    std::vector<std::string> grid;
    std::string line;
    while (std::getline(file, line)) {
        grid.push_back(line);
    }

    std::set<std::pair<int, int> > coords = get_adj_coords(grid);
    
    std::vector<int> nums = get_adj_nums(coords, grid);

    int p_1 = std::accumulate(nums.begin(), nums.end(), 0);

    std::cout << "Coordinates: ";
    for (const auto& coord : coords) {
        std::cout << "(" << coord.first << ", " << coord.second << ") ";
    }
    std::cout << std::endl;
    std::cout << p_1 << std::endl;

    return 0;
}
