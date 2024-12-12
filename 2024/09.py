
import numpy as np

with open("inputs/09.txt") as file:
    map = file.readline()

map = np.array(list(map.strip()))
files = map[::2]
space = map[1::2]


# Part 1

arr = []
id = 0
for f, space in zip(files, space):
    arr += [id] * int(f)
    arr += ["."] * int(space)
    id += 1

if len(files) > len(space):
    arr += [id] * int(files[-1])

arr = np.array(arr)

# print("".join(arr))

left_idx = 0
right_idx = len(arr) - 1

check_sum = 0
while left_idx <= right_idx:
    if arr[left_idx] != ".":
        check_sum += int(arr[left_idx]) * left_idx
        left_idx += 1
    elif arr[right_idx] == ".":
        right_idx -= 1
    else:
        assert arr[left_idx] == "." and arr[right_idx] != "."
        # arr[left_idx] = arr[right_idx]
        # arr[right_idx] = "."
        check_sum += int(arr[right_idx]) * left_idx
        left_idx += 1
        right_idx -= 1

# print("".join(arr))

print(check_sum)

# Part 2


