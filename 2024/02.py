
with open("inputs/02.txt") as f:
    lines = f.readlines()

reports = [
    [int(x) for x in line.strip().split(" ")]
    for line in lines
]

# Part 1
def is_safe(arr) -> bool:
    # All descending or ascending
    if arr[0] > arr[1]:
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                return False
    else:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
    
    # At least 1 or at max 3 delta between each number
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > 3 or abs(arr[i] - arr[i - 1]) == 0:
            return False
        
    return True
        
res = 0
for level in reports:
    if is_safe(level):
        res += 1

print(res)

# Part 2

res = 0
for level in reports:
    if is_safe(level):
        res += 1
        continue
    for idx in range(len(level)):
        level_ = level.copy()
        level_.pop(idx)
        if is_safe(level_):
            res += 1
            break

print(res)