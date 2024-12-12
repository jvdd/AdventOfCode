
with open("inputs/06.txt") as file:
    map = file.readlines()

map = [list(line.strip()) for line in map]

# Part 1

def on_map(pos):
    return 0 <= pos[0] < len(map) and 0 <= pos[1] < len(map[0])

def get_next_idx(char, pos):
    if char == "^":
        return (pos[0] - 1, pos[1])
    elif char == "v":
        return (pos[0] + 1, pos[1])
    elif char == "<":
        return (pos[0], pos[1] - 1)
    elif char == ">":
        return (pos[0], pos[1] + 1)
    
def turn_right(char):
    if char == "^":
        return ">"
    elif char == ">":
        return "v"
    elif char == "v":
        return "<"
    elif char == "<":
        return "^"


char = "^"
for idx, line in enumerate(map):
    if "^" in line:
        pos = (idx, line.index("^"))
        start_pos = (idx, line.index("^"))
        break


locations = set()
locations.add(pos)

while on_map(pos):
    next_pos = get_next_idx(char, pos)
    if not on_map(next_pos):
        break
    next_char = map[next_pos[0]][next_pos[1]]
    if next_char == "#":
        char = turn_right(char)
    else:
        pos = next_pos
        map[pos[0]][pos[1]] = "X"
        locations.add(pos)
        
print(len(locations))

# Part 2

locations = set()

def check_loop(
    block_pos,
):
    loop_blocks = set()
    pos = start_pos
    char = "^"
    while on_map(pos):
        next_pos = get_next_idx(char, pos)
        if not on_map(next_pos):
            break
        if map[next_pos[0]][next_pos[1]] == "#" or next_pos == block_pos:
            if (char, next_pos) in loop_blocks:
                return True
            loop_blocks.add((char, next_pos))
            char = turn_right(char)
        else:
            pos = next_pos
    return False

for row_idx in range(len(map)):
    for col_idx in range(len(map[0])):
        if map[row_idx][col_idx] == "X" and (row_idx, col_idx) != start_pos:
            if check_loop((row_idx, col_idx)):
                locations.add((row_idx, col_idx))

print(len(locations))

