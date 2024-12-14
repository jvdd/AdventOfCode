
with open("inputs/14.txt") as file:
    data = file.readlines()

data = list(map(lambda x: x.strip().split(" "), data))
start_points = [tuple(map(int, e[0].lstrip("p=").split(","))) for e in data]
velocities = [tuple(map(int, e[1].lstrip("v=").split(","))) for e in data]

H = 103
W = 101

def get_points(start_points, velocities, t):
    positions =  [
        (x + vx*t, y + vy*t) 
        for (x, y), (vx, vy) in zip(start_points, velocities)
    ]
    # wrap around edges
    return [(x % W, y % H) for x, y in positions]

# Part 1

points = get_points(start_points, velocities, 100)

def get_quadrant(point):
    x, y = point
    return (0 if x < W//2 and y < H//2 else
            1 if x > W//2 and y < H//2 else
            2 if x < W//2 and y > H//2 else
            3 if x > W//2 and y > H//2 else
            None)

quadrant_count = {q: 0 for q in range(4)}
for point in points:
    q = get_quadrant(point)
    if q is not None:
        quadrant_count[q] += 1

res = 1
for count in quadrant_count.values():
    res *= count

print(res)


# Part 2    

import numpy as np

def neighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

t = 0
points = start_points
while True:
    t += 1
    points = get_points(points, velocities, 1)
    mask = np.random.randn(H, W)  # diff of random numbers is not zero
    for x, y in points:
        mask[y, x] = 100  # diff of neighbouring positions will be zero

    h_diff = np.diff(mask, axis=0)
    w_diff = np.diff(mask, axis=1)
    mask = (h_diff[:H-1,:W-1] + w_diff[:H-1,:W-1] == 0)
    if np.sum(mask) > 100:  # If total contiguous area > 100
        print(t)
        
        grid = [["." for _ in range(W)] for _ in range(H)]
        for x, y in points:
            if grid[y][x] == ".":
                grid[y][x] = 1
            else:
                grid[y][x] += 1
        for row in grid:
            print("".join(map(str, row)))

        break
