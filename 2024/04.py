
with open("inputs/04.txt") as f:
    lines = f.readlines()


# Part 1

res = 0

def get_count(line: str) -> int:
    return line.count("XMAS") + line.count("SAMX")

# 1. iterate over the rows
for line in lines:
    res += get_count(line.strip())
# 2. iterate over the columns
for col_idx in range(len(lines[0].strip())):
    res += get_count("".join([line[col_idx] for line in lines]))

# 3. iterate over the diagonals (left to right)
# 3.1 iterate over the diagonals starting from the first column
for row_idx in range(len(lines)):
    nb = len(lines[0].strip()) - row_idx
    if nb < 4:
        continue
    idxs = [(row_idx + i, i) for i in range(nb)]
    # print("".join([lines[idx[0]][idx[1]] for idx in idxs]))
    res += get_count("".join([lines[idx[0]][idx[1]] for idx in idxs]))
# 3.2 iterate over the diagonals starting from the first row
for col_idx in range(1, len(lines[0].strip())):
    nb = len(lines[0].strip()) - col_idx
    if nb < 4:
        continue
    idxs = [(i, col_idx + i) for i in range(nb)]
    # print("".join([lines[idx[0]][idx[1]] for idx in idxs]))
    res += get_count("".join([lines[idx[0]][idx[1]] for idx in idxs]))
# 4. iterate over the diagonals (right to left)
# 4.1 iterate over the diagonals starting from the last column
for row_idx in range(len(lines)):
    nb = row_idx + 1
    if nb < 4:
        continue
    idxs = [(row_idx - i, i) for i in range(nb)]
    # print("".join([lines[idx[0]][idx[1]] for idx in idxs]))
    res += get_count("".join([lines[idx[0]][idx[1]] for idx in idxs]))
# 4.2 iterate over the diagonals starting from the last row
for col_idx in range(1, len(lines[0].strip())):
    nb = len(lines[0].strip()) - col_idx
    if nb < 4:
        continue
    idxs = [(len(lines) - 1 - i, col_idx + i) for i in range(nb)]
    # print("".join([lines[idx[0]][idx[1]] for idx in idxs]))
    res += get_count("".join([lines[idx[0]][idx[1]] for idx in idxs]))
    
print(res)

# Part 2

res = 0

def is_x_mas(row_idx, col_idx) -> bool:
    left_mas = (
        lines[row_idx-1][col_idx-1] == "M" and lines[row_idx+1][col_idx+1] == "S"
    ) or (
        lines[row_idx-1][col_idx-1] == "S" and lines[row_idx+1][col_idx+1] == "M"
    )
    right_mas = (
        lines[row_idx-1][col_idx+1] == "M" and lines[row_idx+1][col_idx-1] == "S"
    ) or (
        lines[row_idx-1][col_idx+1] == "S" and lines[row_idx+1][col_idx-1] == "M"
    )
    return left_mas and right_mas

for row_idx in range(1, len(lines) - 1):
    for col_idx in range(1, len(lines[0].strip()) - 1):
        if lines[row_idx][col_idx] == "A":
            if is_x_mas(row_idx, col_idx):
                res += 1

print(res)
