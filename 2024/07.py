
import itertools
from tqdm.auto import tqdm

with open("inputs/07.txt") as file:
    data = file.readlines()

test_values = [int(line.strip().split(":")[0]) for line in data]
values = [line.strip().split(":")[1].strip().split(" ") for line in data]

# Part 1

def create_combinations(start, values, operators=["+", "*"]):
    if len(values) == 1:
        return [[*start, values[0]], [*start, values[0]]]
    elif start is None:
        return [
            create_combinations([values[0], op], values[1:], operators)
            for op in operators
        ]
    else:
        return [
            create_combinations([*start, values[0], op], values[1:], operators)
            for op in operators
        ]

def flatten(combinations):
    while any(isinstance(comb[0], list) for comb in combinations):
        combinations = list(itertools.chain.from_iterable(combinations))
    return combinations

# Part 1

res = 0

for v_list, test_val in tqdm(zip(values, test_values), total=len(values)):
    for comb in flatten(create_combinations(None, v_list)):
        comb_eval = int(comb[0])
        for i in range(1, len(comb), 2):
            if comb[i] == "+":
                comb_eval += int(comb[i + 1])
            elif comb[i] == "*":
                comb_eval *= int(comb[i + 1])
        if comb_eval == test_val:
            res += test_val
            # print(test_val, comb)
            break

print(res)
    
# Part 2

res = 0

for v_list, test_val in tqdm(zip(values, test_values), total=len(values)):
    for comb in flatten(create_combinations(None, v_list, ["+", "*", "|"])):
        comb_eval = int(comb[0])
        for i in range(1, len(comb), 2):
            if comb[i] == "+":
                comb_eval += int(comb[i + 1])
            elif comb[i] == "*":
                comb_eval *= int(comb[i + 1])
            elif comb[i] == "|":
                comb_eval = int(str(comb_eval) + comb[i + 1])
        if comb_eval == test_val:
            res += test_val
            # print(test_val, comb)
            break

print(res)