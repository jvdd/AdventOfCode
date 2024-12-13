
with open('inputs/11.txt') as file:
    data = list(map(int, file.read().strip().split()))


# Part 1

# Basic implementation using a list - just like the example
def apply_rule_list(stones: list) -> list:
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones += [1]
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid_idx = len(str_stone) // 2
            new_stones += [
                int(str_stone[:mid_idx]), 
                int(str_stone[mid_idx:]),
            ]
        else:
            new_stones += [stone * 2024]
    return new_stones

stones = data.copy()

for _ in range(25):
    stones = apply_rule_list(stones)

print(len(stones))

# Part 2

# More efficient implementation using a dictionary (saves memory and operations)
def apply_rule_dict(stones: dict) -> dict:
    new_stones = {}
    for stone, nb in stones.items():
        if stone == 0:
            new_idx_list = [1]
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid_idx = len(str_stone) // 2
            new_idx_list = [
                int(str_stone[:mid_idx]), 
                int(str_stone[mid_idx:]),
            ]
        else:
            new_idx_list = [stone * 2024]
        for new_idx in new_idx_list:
            if new_idx in new_stones:
                new_stones[new_idx] += nb
            else:
                new_stones[new_idx] = nb
    return new_stones

stones = {}
for stone in data:
    if stone in stones:
        stones[stone] += 1
    else:
        stones[stone] = 1

for _ in range(75):
    stones = apply_rule_dict(stones)

print(sum(stones.values()))

