
import numpy as np

with open("inputs/09.txt") as file:
    map = file.readline()

map = np.array(list(map.strip()))
files = map[::2]
spaces = map[1::2]


# Part 1

arr = []
id = 0
for f, space in zip(files, spaces):
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

arr = []
id = 0
for f, space in zip(files, spaces):
    arr += [(id, int(f))]
    arr += [(".", int(space))]
    id += 1

if len(files) > len(space):
    arr += [(id, int(files[-1]))]

right_idx = len(arr) - 1
while right_idx >= 0:
    arr_el = arr[right_idx]
    if arr_el[0] != ".":
        el_len = arr_el[1]
        left_idx = 0
        while left_idx < right_idx:
            search_el = arr[left_idx]
            if search_el[0] == "." and search_el[1] >= el_len:
                arr[left_idx] = (arr_el[0], el_len)
                if search_el[1] > el_len:
                    arr.insert(left_idx + 1, (".", search_el[1] - el_len))
                    right_idx += 1
                arr[right_idx] = (".", el_len)
                break
            else:
                left_idx += 1
    right_idx -= 1

# arr_str = []
# for el in arr:
#     arr_str += [str(el[0])] * el[1]
# print("".join(arr_str))

check_sum = 0
idx = 0
for el in arr:
    if el[0] != ".":
        el_len = el[1]
        while el_len > 0:
            check_sum += el[0] * idx
            idx += 1
            el_len -= 1
    else:
        idx += el[1]

print(check_sum)
