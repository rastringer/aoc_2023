# Using long variable names to make clear what's happening!

# Let's make the code more modular vs part 1 

def read_grid_from_file(file_path):
    with open(file_path) as file:
        return file.read().splitlines()

"""Grid is a list of lines:

['.....489............................152....503.........................180......200.........147.......13.......................239..........', '......*.....186.48....681...732........*..................935.........*.....................*......................512............*..874....', '..806.540......*.........*............249......904...358....*......957..867..863..........857.....264..............@....89=......97..*......',...]

"""

# Check for out of bounds
def is_digit_or_oob(grid, row, col):
    return (
        row < 0
        or row >= len(grid)
        or col < 0
        or col >= len(grid[row])
        or not grid[row][col].isdigit()
    )

# Extract the int from coordinates
def extract_num_from_pos(grid, row, col):
    start = ""
    while col < len(grid[row]) and grid[row][col].isdigit():
        start += grid[row][col]
        col += 1
    return int(start)

# Find adjacents
def find_adjacent_coords(grid, row_coords, col_coords):
    coords = set()
    for current_row in range(row_coords -1, row_coords + 2):
        for current_col in range(col_coords -1, col_coords + 2):
            if is_digit_or_oob(grid, current_row, current_col):
                continue
            while current_col > 0 and grid[current_row][current_col - 1].isdigit():
                current_col -= 1
            coords.add((current_row, current_col))
    return coords 
   
def get_adj_coords(grid):
    total = 0
    # the row index / coordinates of each row
    for row_coords, row in enumerate(grid):
        # same for column coordinates for each character in the row
        for col_coords, char in enumerate(row):
            # skip if character isn't a * gear symbol
            if char != '*':
                continue
            # Coordinates to keep track of gears this time
            coords = find_adjacent_coords(grid, row_coords, col_coords)
            if len(coords) == 2:
                print(f"coords={coords}")
                nums = [extract_num_from_pos(grid, row, col) for row, col in coords] 
                print(f"nums={nums}")
                total += nums[0] * nums[1]

    return total

grid = read_grid_from_file("input.txt")
p_2 = get_adj_coords(grid)
print(p_2)
# 72553319