from collections import defaultdict

with open("input.txt") as f:
    lines = []
    for line in f:
        cleaned_line = line.rstrip("\n") 
        lines.append(cleaned_line)
    
actuals = {"red": 12, "green": 13, "blue": 14}
p2_result = 0 

for line in lines:
    game_possible = True
    game_id, line = line.split(":")
    games_dict = defaultdict(int)
    for turn in line.split(";"):
        #  3 green, 1 blue
        #  7 blue, 3 red, 5 green
        #  1 green, 5 blue
        #  etc
        for cubes in turn.split(","):
            n, color = cubes.split()
            n = int(n)
            games_dict[color] = max(games_dict[color], n)
            # Get the max cube numbers eg:
            # 6 blue, 2 green; 3 green, 4 blue; 10 green, 1 blue = 
            # defaultdict(<class 'int'>, {'blue': 6, 'red': 0, 'green': 10})
            for color, actual_val in actuals.items():
                actual_val = int(actual_val)
                val = games_dict[color]
                val = int(val)
                if val > actual_val:
                    game_possible = False

    # Part 2: since we already worked out the max values from the 
    # games played with (max(games_dict[color], n)), we just have to 
    # find the product for those values, then add them. 
    product = 1
    for value in games_dict.values():
            product *= value

    p2_result += product
    print(p2_result)
    # 76008 (other data will give a different answer)
    
    

    




