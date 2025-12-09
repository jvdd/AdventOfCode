with open("inputs/06.txt") as f:
    lines = f.readlines()

lines_stripped = [line.strip().replace("    ", " ").replace("   ", " ").replace("  ", " ") for line in lines]

values = [line.strip().split(" ") for line in lines_stripped[:-1]]
operations = lines_stripped[-1].split(" ")

# --- Part 1
results = []
for ix, op in enumerate(operations):
    results += [eval(op.join([v[ix] for v in values]))]
print(sum(results))

# --- Part 2
results = []
values = []
for col_ix in range(len(lines[0])):
    value = "".join(row[col_ix] for row in lines[:-1] if row[col_ix].strip()).strip()
    values.append(value)

ix = 0
results = []
for op in operations:
    op_values = []
    while values[ix].strip() != "":
        op_values.append(values[ix])
        ix += 1
    results.append(eval(op.join(op_values)))
    ix += 1  # skip empty line
print(sum(results))