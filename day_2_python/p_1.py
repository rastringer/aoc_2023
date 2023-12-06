from collections import defaultdict

with open("input.txt") as f:
    lines = []
    for line in f:
        cleaned_line = line.rstrip("\n") 
        lines.append(cleaned_line)
    
actuals = {"red": 12, "green": 13, "blue": 14}
p1_result = 0 

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
            # defaultdict(<class 'int'>, {'blue': 6, 'red': 0, 'green': 10})
            # etc
            for color, actual_val in actuals.items():
                actual_val = int(actual_val)
                val = games_dict[color]
                val = int(val)
                if val > actual_val:
                    game_possible = False

    if game_possible:
        p1_result += int(game_id.split()[-1])
    
    print(p1_result)
    # 2348 (for my inputs, yours will be different)




