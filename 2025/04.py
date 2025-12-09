with open("inputs/04.txt") as f:
    lines = f.readlines()

lines = [list(line.strip()) for line in lines]

def replace_accessible():
    accessible_positions = []
    for row in range(len(lines)):
        line = lines[row]
        for col in range(len(line)):
            if line[col] != "@":
                continue
            surrounding_positions = [
                (row-1, col-1), (row-1, col), (row-1, col+1),
                (row, col-1),                 (row, col+1),
                (row+1, col-1), (row+1, col), (row+1, col+1),
            ]
            counts = 0
            for r, c in surrounding_positions:
                if r < 0 or r >= len(lines):
                    continue
                if c < 0 or c >= len(lines[r]):
                    continue
                if lines[r][c] == "@":
                    counts += 1
            if counts < 4:
                accessible_positions.append((row, col))

    return accessible_positions


# --- Part 1
accessible_positions = replace_accessible()
print(len(accessible_positions))

# --- Part 2
while len(accessible_positions) > 0:
    for r, c in accessible_positions:
        lines[r][c] = "x"
    accessible_positions = replace_accessible()

print(sum(line.count("x") for line in lines))
