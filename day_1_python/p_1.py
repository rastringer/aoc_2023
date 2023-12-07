# Part One

with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0

for l in lines:
    digits = []
    for c in l:
        if c.isdigit():
            digits.append(c)
    concat = int(digits[0]+digits[-1])
    total += concat


print(total)   
#54644 (answers are unique)   