
with open("inputs/01.txt") as f:
    lines = f.readlines()

arr1 = []
arr2 = []
for line in lines:
    line = line.strip().split("   ")
    assert len(line) == 2
    arr1.append(int(line[0]))
    arr2.append(int(line[1]))

# Part 1
arr1 = sorted(arr1)
arr2 = sorted(arr2)

res = 0
for i in range(len(arr1)):
    res += abs(arr1[i] - arr2[i])

print(res)

# Part 2
res = 0
right_idx = 0
for nb in arr1:
    while right_idx < len(arr2) and arr2[right_idx] < nb:
        right_idx += 1
    while right_idx < len(arr2) and arr2[right_idx] == nb:
        res += nb
        right_idx += 1

print(res)
