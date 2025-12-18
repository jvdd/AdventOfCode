with open("inputs/07.txt") as f:
    lines = f.readlines()

hor_beam_pos = [i for i in range (len(lines[0].strip())) if lines[0][i] == "S"]

# --- Part 1
n_splits = 0
for line in lines[1:]:
    new_beam_pos = set()
    for pos in hor_beam_pos:
        if line[pos] == ".":
            new_beam_pos.add(pos)
        elif line[pos] == "^":
            n_splits += 1
            new_beam_pos.add(pos - 1)
            new_beam_pos.add(pos + 1)
    hor_beam_pos = sorted(list(new_beam_pos))

print(n_splits)

# --- Part 2
n_paths = [1 if char == "S" else 0 for char in lines[0].strip()]
for line in lines[1:]:
    new_n_paths = [0] * len(line.strip())
    for pos in range(len(line.strip())):
        if line[pos] == ".":
            new_n_paths[pos] += n_paths[pos]
        elif line[pos] == "^":
            if pos > 0:
                new_n_paths[pos - 1] += n_paths[pos]
            if pos < len(line) - 1:
                new_n_paths[pos + 1] += n_paths[pos]
    n_paths = new_n_paths

print(sum(n_paths))