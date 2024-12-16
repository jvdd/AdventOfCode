
import numpy as np

with open("inputs/15.txt") as file:
    map = []
    while (line := file.readline().strip()) != "":
        map += [list(line)]
    instructions = []
    while (line := file.readline().strip()) != "":
        instructions += list(line.strip())

map_orig = np.array(map)
H, W = map_orig.shape

def get_next_direction(x, y, move):
    if move == "^":
        return x - 1, y
    if move == "v":
        return x + 1, y
    if move == "<":
        return x, y - 1
    if move == ">":
        return x, y + 1
    raise ValueError("Invalid move")

# Part 1
def move_robot(x, y, direction):
    next_x, next_y = get_next_direction(x, y, direction)
    if map[next_x][next_y] == "#":  # No move (because of wall)
        return x, y
    elif map[next_x][next_y] == ".":  # Move to empty space
        return next_x, next_y
    else:
        assert map[next_x][next_y] == "O"
        vec_x, vec_y = next_x - x, next_y - y
        assert vec_x == 0 or vec_y == 0
        assert vec_x != 0 or vec_y != 0
        x_o, y_o = next_x, next_y
        while map[x_o][y_o] == "O":
            x_o += vec_x
            y_o += vec_y
        if map[x_o][y_o] == "#":
            return x, y
        else:
            assert map[x_o][y_o] == "."
            map[x_o][y_o] = "O"
            return next_x, next_y

map = map_orig.copy()

start_x, start_y = np.where(map == "@")
assert len(start_x) == 1 and len(start_y) == 1
x, y = start_x[0], start_y[0]

# print("Start", x, y)
for move in instructions:
    map[x][y] = "."
    # print(move, x, y, "->", end=" ")
    x, y = move_robot(x, y, move)
    # print(x, y)
    map[x][y] = "@"
    # for row in map:
    #     print("".join(row))
    # print()

res = 0
for x in range(H):
    for y in range(W):
        if map[x][y] == "O":
            res += x * 100 + y
print(res)


# Part 2
def move_robot(r_x, r_y, direction):
    next_x, next_y = get_next_direction(r_x, r_y, direction)
    if map[next_x][next_y] == "#":  # No move (because of wall)
        return r_x, r_y
    elif map[next_x][next_y] == ".":  # Move to empty space
        return next_x, next_y
    else:
        assert map[next_x][next_y] in ["[", "]"]
        vec_x, vec_y = next_x - r_x, next_y - r_y
        assert vec_x == 0 or vec_y == 0
        assert vec_x != 0 or vec_y != 0
        if vec_y != 0:
            x_o, y_o = next_x, next_y + vec_y
            while map[x_o][y_o] in ["[", "]"]:
                y_o += vec_y
            if map[x_o][y_o] == "#":
                return r_x, r_y
            else:
                assert map[x_o][y_o] == "."
                if vec_y == 1:
                    iter = range(next_y+1, y_o+1, 2)
                elif vec_y == -1:
                    iter = range(y_o, next_y, 2)
                for y_ in iter:
                    map[x_o][y_] = "["
                    map[x_o][y_ + 1] = "]"
                return next_x, next_y
        else:
            next_points = set([(next_x, next_y)])
            seen_points = set()
            if map[next_x][next_y] == "[":
                assert map[next_x][next_y + 1] == "]"
                next_points.add((next_x, next_y + 1))
            else:
                assert map[next_x][next_y] == "]"
                next_points.add((next_x, next_y - 1))
            while any(map[x][y] in ["[", "]"] for (x, y) in next_points):
                new_next_points = set()
                for nx, ny in next_points.copy():
                    if map[nx][ny] == "[":
                        assert map[nx][ny + 1] == "]"
                        new_next_points.add((nx + vec_x, ny))
                        if (nx, ny + 1) not in next_points:
                            next_points.add((nx, ny + 1))
                            new_next_points.add((nx + vec_x, ny + 1))
                    elif map[nx][ny] == "]":
                        new_next_points.add((nx + vec_x, ny))
                        assert map[nx][ny - 1] == "["
                        if (nx, ny - 1) not in next_points:
                            next_points.add((nx, ny - 1))
                            new_next_points.add((nx + vec_x, ny - 1))
                    elif map[nx][ny] == "#":
                        return r_x, r_y
                    else:
                        assert map[nx][ny] == "."
                        new_next_points.add((nx, ny))
                seen_points.update(next_points)
                next_points = new_next_points
            if any(map[x][y] == "#" for (x, y) in next_points):
                return r_x, r_y
            if vec_x == 1:
                iter = range(W*2, 0, -1)
            elif vec_x == -1:
                iter = range(W*2)
            seen_points = set(p for p in seen_points if map[p[0], p[1]] in ["[", "]"])
            for r_x in iter:
                x_points = [p for p in seen_points if p[0] == r_x]
                for p in x_points:
                    value = map[p[0], p[1]]
                    map[p[0], p[1]] = "."
                    map[p[0] + vec_x, p[1]] = value
            return next_x, next_y

map = np.repeat(map_orig, 2, axis=1)
for x in range(1, H-1):
    y = 2
    while y < W * 2 - 2:
        if map[x][y] == "O":
            assert map[x][y + 1] == "O"
            map[x][y] = "["
            map[x][y + 1] = "]"
            y += 1
        elif map[x][y] == "@":
            assert map[x][y + 1] == "@"
            map[x][y+1] = "."
        y += 1

start_x, start_y = np.where(map == "@")
assert len(start_x) == 1 and len(start_y) == 1
x, y = start_x[0], start_y[0]

for move in instructions:
    map[x][y] = "."
    # print(move, x, y, "->", end=" ")
    x, y = move_robot(x, y, move)
    # print(x, y)
    map[x][y] = "@"
    # for row in map:
    #     print("".join(row))
    
res = 0
for x in range(H):
    for y in range(W*2):
        if map[x][y] == "[":
            res += x * 100 + y
print(res)