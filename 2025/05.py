
ranges = []
values = []
empty_line_seen = False
with open("inputs/05.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line == "":
            empty_line_seen = True
            continue
        if not empty_line_seen:
            ranges.append(tuple(map(int, line.split("-"))))
        else:
            values.append(int(line))

ranges = sorted(ranges, key=lambda x: x[0])

# --- Part 1
fresh_values = []
for val in values:
    is_fresh = False
    for start, end in ranges:
        if start <= val <= end:
            is_fresh = True
            break
    if is_fresh:
        fresh_values.append(val)

print(len(fresh_values))

# --- Part 2
reduced = True
while reduced:
    reduced = False
    new_ranges = []
    for idx in range(len(ranges)):
        start, end = ranges[idx]
        if len(new_ranges) == 0:
            new_ranges.append((start, end))
            continue
        last_start, last_end = new_ranges[-1]
        if start <= last_end:
            new_ranges[-1] = (last_start, max(last_end, end))
            reduced = True
        else:
            new_ranges.append((start, end))
    ranges = new_ranges

print(sum(end - start + 1 for start, end in new_ranges))