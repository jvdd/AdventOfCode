
with open("inputs/13.txt") as file:
    data = file.readlines()

idx = len(data) - 1
games = []
while idx > 0:
    prize = data[idx].strip().lstrip("Prize: ")
    prize = tuple(map(lambda p: int(p.split("=")[1]), prize.split(", ")))
    idx -= 1
    button_b = data[idx].strip().lstrip("Button B: ")
    button_b = tuple(map(lambda p: int(p.split("+")[1]), button_b.split(", ")))
    idx -= 1
    button_a = data[idx].strip().lstrip("Button A: ")
    button_a = tuple(map(lambda p: int(p.split("+")[1]), button_a.split(", ")))
    idx -= 1

    games.append((button_a, button_b, prize))

    # skip empty line
    idx -= 1

games = games[::-1]

# Part 1

res = 0
for (a_x, a_y), (b_x, b_y), (p_x, p_y) in games:
    # A * a_x + B * b_x = p_x
    # A * a_y + B * b_y = p_y
    A = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
    B = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)

    A, B = int(A), int(B)
    if A * a_x + B * b_x != p_x or A * a_y + B * b_y != p_y:
        # solution is not integer
        continue

    res += 3*A + 1*B

print(res)

# Part 2

res = 0
for (a_x, a_y), (b_x, b_y), (p_x, p_y) in games:
    p_x, p_y = p_x + 10000000000000, p_y + 10000000000000
    A = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
    B = (a_x * p_y - a_y * p_x) / (a_x * b_y - a_y * b_x)

    A, B = int(A), int(B)
    if A * a_x + B * b_x != p_x or A * a_y + B * b_y != p_y:
        # solution is not integer
        continue

    # print(f"A = {A}, B = {B}")
    res += 3*A + 1*B

print(res)
