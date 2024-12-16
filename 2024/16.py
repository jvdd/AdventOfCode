
import numpy as np

with open("inputs/16.txt") as file:
    data = file.readlines()

data = np.array([list(line.strip()) for line in data])

start_x, start_y = np.where(data == "S")
assert len(start_x) == 1 and len(start_y) == 1
start_x, start_y = start_x[0], start_y[0]

def get_next_idx(x, y, move):
    if move == "^":
        return x - 1, y
    if move == "v":
        return x + 1, y
    if move == "<":
        return x, y - 1
    if move == ">":
        return x, y + 1
    raise ValueError("Invalid move")

def get_move_options(move):
    if move == "^":
        return ["^", "<", ">"]
    if move == "v":
        return ["v", "<", ">"]
    if move == "<":
        return ["<", "^", "v"]
    if move == ">":
        return [">", "^", "v"]
    raise ValueError("Invalid move")

stack = [(start_x, start_y, ">", 0, [(start_x, start_y)])]
visited = {}
min_solution = float("inf")
solutions = []
while stack:
    # pop the first element of the stack (should have lower cost)
    x, y, direction, cost, pos_list = stack.pop(0)
    if cost > min_solution:
        continue
    if data[x][y] == "E":
        if cost < min_solution:
            solutions = []
            solutions += [pos_list]
            min_solution = cost
        elif cost == min_solution:
            solutions += [pos_list]
    if (x, y, direction) in visited and visited[(x, y, direction)] < cost:
        continue
    visited[(x, y, direction)] = cost
    for move in get_move_options(direction):
        if move == direction:
            next_x, next_y = get_next_idx(x, y, move)
            if data[next_x][next_y] != "#":
                # insert low cost moves to the beginning of the stack
                stack.insert(0, (next_x, next_y, move, cost + 1, pos_list + [(next_x, next_y)]))
        else:
            # append high cost moves to the end of the stack
            stack.append((x, y, move, cost + 1000, pos_list))

# Part 1
print(min_solution)

# Part 2
tiles = set()
for solution in solutions:
    tiles.update(set(solution))
print(len(tiles))