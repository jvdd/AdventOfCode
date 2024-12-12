
import numpy as np

with open('inputs/10.txt') as f:
    data = f.readlines()

data = np.array([list(map(int, x.strip())) for x in data])

def find_next(x, y):
    next_value = data[x, y] + 1
    res = []
    idxs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for x, y in idxs:
        if x < 0 or x >= data.shape[0] or y < 0 or y >= data.shape[1]:
            continue
        if data[x, y] == next_value:
            res += [(x, y)]
    return res

# Part 1

x_idx, y_idx = np.where(data == 0)

score = 0
for x, y in zip(x_idx, y_idx):
    options = [(x, y)]
    for v in range(9):
        new_options = []
        for x, y in options:
            assert data[x, y] == v
            new_options += find_next(x, y)
        options = set(new_options)
    score += len(options)
print(score)
    

# Part 2

options = [(x, y) for x, y in zip(x_idx, y_idx)]
for v in range(9):
    new_options = []
    for x, y in options:
        assert data[x, y] == v
        new_options += find_next(x, y)
    options = new_options

print(len(options))