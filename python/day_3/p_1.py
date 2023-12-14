# Using long variable names to make clear what's happening!

with open('input.txt') as file:
    grid = file.read().splitlines()

def get_adj_coords(grid):
    # We need to find the coordinations of valid numbers (those adjacent
    # to symbols), and keep track of our them in a set to prevent duplication
    coords = set()
    # the row index / coordinates of each row
    for row_coords, row in enumerate(grid):
        # same for column coordinates for each character in the row
        for col_coords, char in enumerate(row):
            # skip if character isn't a symbol
            if char.isdigit() or char == '.':
                continue
            # once we find a symbol, check the adjacent coordinates
            # surrounding rows
            for current_row in range(row_coords -1, row_coords + 2):
                # surrounding columns
                for current_col in range(col_coords - 1, col_coords + 2):
                    # check for out of bounds
                    if current_row < 0 or current_row >= len(grid) or current_col < 0 or current_col >= len(grid[current_row]) or not grid[current_row][current_col].isdigit():
                        # skip if if OOB or not a digit
                        continue
                    # Crucial part for extracting complete numbers ('47' vs '4', '7')
                    # On finding a digit, move left until character is no longer digit
                    while current_col > 0 and grid[current_row][current_col -1].isdigit():
                        current_col -= 1
                    # add the revelant coordinates to the set
                    coords.add((current_row, current_col))
    return coords

coords = get_adj_coords(grid)
# coords = {(26, 3), (108, 91), (129, 25), (38, 14), (57, 27)...} 

def get_adj_nums(coords):
    nums = []
    for row_coords, col_coords in coords:
        # scan to right and convert values to ints
        start = ""
        while col_coords < len(grid[row_coords]) and grid[row_coords][col_coords].isdigit():
            start += grid[row_coords][col_coords]
            col_coords += 1
        nums.append(int(start))

    return nums 
print(coords)
nums = get_adj_nums(coords)
# nums = [4, 653, 48, 132, 996, 271, 289, 527, 76, 944, 943, 432, 41, 515...etc]
p_1 = sum(nums)
print(p_1)
# 507214