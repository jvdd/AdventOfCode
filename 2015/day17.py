
from itertools import combinations

containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

liters = 150

## Part 1
combs = []
for i in range(3,15):
    for combination in combinations(containers, i):
        if sum(combination) == liters:
            combs.append(combination)

print(len(combs))

## Part 2
combs = {}
for i in range(3,15):
    for combination in combinations(containers, i):
        if sum(combination) == liters:
            if i in combs:
                combs[i] += 1
            else:
                combs[i] = 1

print(combs[min(combs, key=int)])
