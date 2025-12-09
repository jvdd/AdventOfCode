
with open("inputs/03.txt") as f:
    lines = f.readlines()

joltage_12 = 0

def find_max_joltage(line: str, nb_components = 2) -> str:
    if nb_components == 1:
        return max(line)
    # A: brute-force => try all combinations and return the max
    # return max(
    #     line[idx] + find_max_joltage(line[idx+1:], nb_components - 1)
    #     for idx in range(len(line)-nb_components+1)
    # )
    # B: select the best component at each step
    max_current = max(line[:len(line)-nb_components+1])
    max_idx = line.index(max_current)
    return max_current + find_max_joltage(line[max_idx+1:], nb_components - 1)


# --- Part 1

joltage_2 = 0
for line in lines:
    line = line.strip()
    max_joltage = find_max_joltage(line, 2)
    joltage_2 += int(max_joltage)
print(joltage_2)

# --- Part 2

joltage_12 = 0
for line in lines:
    line = line.strip()
    max_joltage = find_max_joltage(line, 12)
    joltage_12 += int(max_joltage)
print(joltage_12)