
with open("inputs/01.txt") as f:
    lines = f.readlines()

# 5941

def process_rotations(rots: list[str]):
    current = 50
    on_zero = 0
    
    pass_zero_count = 0

    for rot in rots:
        direction = rot[0]
        amount = int(rot[1:].strip())
    
        previous = current
        if direction == 'L':
            current -= amount
        elif direction == 'R':
            current += amount
        
        # --- Part 1 ---
        if current % 100 == 0:
            on_zero += 1
        
        # --- Part 2 ---
        change = abs(current // 100 - previous // 100)
        if previous % 100 == 0 and direction == 'L' and amount > 0:
            change = max(0, change - 1)
        if current % 100 == 0 and direction == 'L' and amount > 0:
            change += 1
        pass_zero_count += change
        

    print(on_zero)
    print(pass_zero_count)

# Part 1
process_rotations(lines)