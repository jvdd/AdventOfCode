
import re

with open('inputs/03.txt') as f:
    lines = f.readlines()

lines = " ".join(lines)

# Part 1

regex_str = r'mul\(\d{1,3},\d{1,3}\)'

res = 0
matches = re.findall(regex_str, lines)
for match in matches:
    match = match.split('(')[1].split(')')[0]
    a, b = match.split(',')
    res += int(a) * int(b)

print(res)

# Part 2

matches = re.findall(regex_str + r"|do\(\)" + r"|don't\(\)", lines)

res = 0
do = True
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    else:
        if do:
            match = match.split('(')[1].split(')')[0]
            a, b = match.split(',')
            res += int(a) * int(b)

print(res)



