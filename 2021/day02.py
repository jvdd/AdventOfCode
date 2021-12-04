inp = open("input/inputDay02.txt")
course = [tuple(l.strip().split(" ")) for l in inp.readlines()]
inp.close()

# Part 1
horiz = 0; depth = 0;
for (dir, amount) in course:
    if dir == "forward":
        horiz += int(amount)
    elif dir == "up":
        depth -= int(amount)
    elif dir == "down":
        depth += int(amount)
    
print(horiz*depth)

# Part 2
horiz = 0; depth = 0; aim = 0;
for (dir, amount) in course:
    if dir == "forward":
        horiz += int(amount)
        depth += aim*int(amount)
    elif dir == "up":
        aim -= int(amount)
    elif dir == "down":
        aim += int(amount)
    
print(horiz*depth)