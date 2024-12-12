
with open("inputs/05.txt") as f:
    lines = f.readlines()

constraits = {}
for line in lines:
    if "|" in line:
        k, v = tuple(line.strip().split("|"))
        if k in constraits:
            constraits[k].append(v)
        else:
            constraits[k] = [v]

lines = [line.strip().split(",") for line in lines if "," in line]

# Part 1


def is_correct(line):
    for idx in range(len(line)):
        nb = line[idx]
        if nb in constraits:
            if any(prec in line[:idx] for prec in constraits[nb]):
                return False
    return True

res = 0
for line in lines:
    if is_correct(line):
        res += int(line[len(line) // 2])
print(res)

# Part 2


def fixorder(line):
    for idx in range(len(line)):
        nb = line[idx]
        if nb in constraits:
            for prec in constraits[nb]:
                if prec in line[:idx]:
                    prec_idx = line.index(prec)
                    line = line[:prec_idx] + [nb] + line[prec_idx:idx] + line[idx + 1:]
                    return fixorder(line)
    return line

res = 0
for line in lines:
    if not is_correct(line):
        line = fixorder(line)
        res += int(line[len(line) // 2])
print(res)