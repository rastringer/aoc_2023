# Part Two
with open("input.txt") as f:
    lines = []
    for line in f:
        cleaned_line = line.rstrip("\n") 
        lines.append(cleaned_line)

digit_dict = {"one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }

total = 0
i = 0

for line in lines:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for word in digit_dict:
            if line[i:].startswith(word):
                digits.append(str(digit_dict[word]))
    concat = int(digits[0] + digits[-1])
    total += concat

print(total)
#53348