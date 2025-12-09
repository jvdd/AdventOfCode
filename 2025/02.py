
with open("inputs/02.txt") as f:
    lines = f.readlines()

assert len(lines) == 1
ranges = lines[0].strip().split(",")
print(ranges)

# --- Part 1

invalid_ids = []

def get_invalid_ids(start: int, end: int) -> list[int]:
    invalids = []
    for i in range(start, end + 1):
        str_id = str(i)
        sub_str1 = str_id[:len(str_id)//2]
        sub_str2 = str_id[len(str_id)//2:]
        if sub_str1 == sub_str2:
            invalid_ids.append(i)
    return invalids

for ids in ranges:
    first, second = ids.split("-")
    invalid_ids += get_invalid_ids(int(first), int(second))

print(sum(invalid_ids))

# --- Part 2

invalid_ids = []

def get_invalid_ids_v2(start: int, end: int) -> list[int]:
    invalids = []
    for i in range(start, end + 1):
        str_id = str(i)
        for idx in range(1, len(str_id) // 2 + 1):
            if len(str_id) % idx != 0:
                continue
            pattern = str_id[:idx]
            repeated = pattern * (len(str_id) // idx)
            assert len(repeated) == len(str_id)
            if repeated == str_id:
                invalids.append(i)
                break
    return invalids

for ids in ranges:
    first, second = ids.split("-")
    invalid_ids += get_invalid_ids_v2(int(first), int(second))

print(sum(invalid_ids))
    

    