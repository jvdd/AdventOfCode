
import numpy as np
import math
from itertools import combinations

with open("inputs/08.txt") as file:
    map = file.readlines()

map = np.array([list(line.strip()) for line in map])
antennas = np.unique(map)

# Part 1

locations = set()

for antenna in antennas:
    if antenna == ".":
        continue
    idxs = list(zip(*np.where(map == antenna)))
    for (a1, a2) in combinations(idxs, 2):
        x_diff = abs(a2[0] - a1[0])
        y_diff = abs(a2[1] - a1[1])
        if a1[0] < a2[0]:
            if a1[1] < a2[1]:
                locations.add((a1[0] - x_diff, a1[1] - y_diff))
                locations.add((a2[0] + x_diff, a2[1] + y_diff))
            else:
                locations.add((a1[0] - x_diff, a1[1] + y_diff))
                locations.add((a2[0] + x_diff, a2[1] - y_diff))
        else:
            if a1[1] < a2[1]:
                locations.add((a1[0] + x_diff, a1[1] - y_diff))
                locations.add((a2[0] - x_diff, a2[1] + y_diff))
            else:
                locations.add((a1[0] + x_diff, a1[1] + y_diff))
                locations.add((a2[0] - x_diff, a2[1] - y_diff))

# prune locations to only those within the map
locations = set(filter(lambda x: 0 <= x[0] < map.shape[0] and 0 <= x[1] < map.shape[1], locations))

print(len(locations))
    
# Part 2

locations = set()

for antenna in antennas:
    if antenna == ".":
        continue
    idxs = list(zip(*np.where(map == antenna)))
    for idx in idxs:
        locations.add(idx)
    for (a1, a2) in combinations(idxs, 2):
        x_diff = abs(a2[0] - a1[0])
        y_diff = abs(a2[1] - a1[1])
        if a1[0] < a2[0]:
            if a1[1] < a2[1]:
                p1 = (a1[0] - x_diff, a1[1] - y_diff)
                while p1[0] >= 0 and p1[1] >= 0:
                    locations.add(p1)
                    p1 = (p1[0] - x_diff, p1[1] - y_diff)
                p2 = (a2[0] + x_diff, a2[1] + y_diff)
                while p2[0] < map.shape[0] and p2[1] < map.shape[1]:
                    locations.add(p2)
                    p2 = (p2[0] + x_diff, p2[1] + y_diff)
            else:
                p1 = (a1[0] - x_diff, a1[1] + y_diff)
                while p1[0] >= 0 and p1[1] < map.shape[1]:
                    locations.add(p1)
                    p1 = (p1[0] - x_diff, p1[1] + y_diff)
                p2 = (a2[0] + x_diff, a2[1] - y_diff)
                while p2[0] < map.shape[0] and p2[1] >= 0:
                    locations.add(p2)
                    p2 = (p2[0] + x_diff, p2[1] - y_diff)
        else:
            if a1[1] < a2[1]:
                p1 = (a1[0] + x_diff, a1[1] - y_diff)
                while p1[0] < map.shape[0] and p1[1] >= 0:
                    locations.add(p1)
                    p1 = (p1[0] + x_diff, p1[1] - y_diff)
                p2 = (a2[0] - x_diff, a2[1] + y_diff)
                while p2[0] >= 0 and p2[1] < map.shape[1]:
                    locations.add(p2)
                    p2 = (p2[0] - x_diff, p2[1] + y_diff)
            else:
                p1 = (a1[0] + x_diff, a1[1] + y_diff)
                while p1[0] < map.shape[0] and p1[1] < map.shape[1] :
                    locations.add(p1)
                    p1 = (p1[0] + x_diff, p1[1] + y_diff)
                p2 = (a2[0] - x_diff, a2[1] - y_diff)
                while p2[0] >= 0 and p2[1] >= 0:
                    locations.add(p2)
                    p2 = (p2[0] - x_diff, p2[1] - y_diff)


print(len(locations))

