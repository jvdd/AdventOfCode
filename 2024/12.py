
import numpy as np

with open('inputs/12.txt') as f:
    data = f.readlines()

data = np.array([list(line.strip()) for line in data])

def get_idx(lst, coord):
    for i in range(len(lst)):
        if coord in lst[i]:
            return i
    return None

def neighbor(a1, a2):
    return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1]) == 1

masks = {crop : [] for crop in np.unique(data)}
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        crop = data[x, y]
        if x > 0 and data[x-1][y] == crop:
            idx = get_idx(masks[crop], (x-1, y))
            if idx is not None:
                masks[crop][idx].append((x, y))
        elif y > 0 and data[x][y-1] == crop:
            idx = get_idx(masks[crop], (x, y-1))
            if idx is not None:
                masks[crop][idx].append((x, y))
        else:
            masks[crop].append([(x, y)])


for crop in masks:
    idx = 0
    while idx < len(masks[crop]):
        mask = masks[crop][idx]
        neighbor_found = False
        for coord in mask:
            for other_mask in masks[crop][:idx] + masks[crop][idx+1:]:
                for other_coord in other_mask:
                    if neighbor(coord, other_coord):
                        mask += other_mask
                        masks[crop][idx] = mask
                        masks[crop].remove(other_mask)
                        neighbor_found = True
                        break
                if neighbor_found:
                    break
            if neighbor_found:
                break
        if not neighbor_found:
            idx += 1

# Part 1

res = 0
for crop, mask_list in masks.items():
    for mask_idx in mask_list:
        mask = np.zeros(data.shape, dtype=bool)
        for x, y in mask_idx:
            mask[x, y] = True

        area = np.sum(mask)
        perimeter  = 0
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if mask[i, j]:
                    if i == 0 or not mask[i-1, j]:
                        perimeter += 1
                    if i == mask.shape[0]-1 or not mask[i+1, j]:
                        perimeter += 1
                    if j == 0 or not mask[i, j-1]:
                        perimeter += 1
                    if j == mask.shape[1]-1 or not mask[i, j+1]:
                        perimeter += 1

        res += area * perimeter

print(res)

# Part 2

res = 0
for crop, mask_list in masks.items():
    for mask_idx in mask_list:
        mask = np.zeros(data.shape, dtype=bool)
        for x, y in mask_idx:
            mask[x, y] = True

        area = np.sum(mask)
        sides = list()
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if mask[i, j]:
                    # need to log orientation and inward direction of side
                    if i == 0 or not mask[i-1, j]:
                        sides.append(("h", i, j, "top"))
                    if i == mask.shape[0]-1 or not mask[i+1, j]:
                        sides.append(("h", i+1, j, "bottom"))
                    if j == 0 or not mask[i, j-1]:
                        sides.append(("v", i, j, "left"))
                    if j == mask.shape[1]-1 or not mask[i, j+1]:
                        sides.append(("v", i, j+1, "right"))

        # reduce the neighboring sides (same orientation & inward direction)
        new_sides = list()
        for side in sides:
            # keep only the rightmost / lowest side of a series of neighboring sides
            if side[0] == "h":
                if ("h", side[1], side[2]+1, side[3]) in sides:
                    continue
            else:
                if ("v", side[1]+1, side[2], side[3]) in sides:
                    continue
            new_sides.append(side)

        res += area * len(new_sides)

print(res)