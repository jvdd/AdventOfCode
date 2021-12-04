import numpy as np

inp = open("input/inputDay03.txt")
report = [list(l.strip()) for l in inp.readlines()]
inp.close()

def binary_to_decimal(arr):
    vals = [2**i for i in range(len(arr))]
    return np.dot(arr, vals)

report = np.array(report).astype(int)

# Part 1
gamma = []; epsilon = [];
for idx in range(report.shape[-1],0,-1):
    vals, counts = np.unique(report[:,idx-1], return_counts=True)
    gamma += [vals[np.argmax(counts)]]
    epsilon += [vals[np.argmin(counts)]]
# epsilon = np.abs(np.array(gamma) - 1)
print(binary_to_decimal(gamma) * binary_to_decimal(epsilon))

# Part 2
oxygen_arr = report.copy()
co2_arr = oxygen_arr = report.copy()
for idx in range(0,report.shape[-1]):
    # Oxygen
    if len(oxygen_arr) > 1:
        vals, counts = np.unique(oxygen_arr[:,idx], return_counts=True)
        val = 1 if counts[0] == counts[1] else vals[np.argmax(counts)]
        oxygen_arr = oxygen_arr[oxygen_arr[:,idx] == val]
    if len(co2_arr) > 1:
        vals, counts = np.unique(co2_arr[:,idx], return_counts=True)
        val = 0 if counts[0] == counts[1] else vals[np.argmin(counts)]
        co2_arr = co2_arr[co2_arr[:,idx] == val]
print(binary_to_decimal(oxygen_arr[0][::-1]) * binary_to_decimal(co2_arr[0][::-1]))