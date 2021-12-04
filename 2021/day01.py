import numpy as np

# Part 1
def larger_than_prev(arr):
    return np.sum(arr[1:]-arr[:-1] > 0)


inp = open("input/inputDay01.txt")
numbers = np.array([int(l.strip()) for l in inp.readlines()])
inp.close()

print(larger_than_prev(numbers))

# Part 2
numbers = numbers + np.hstack([numbers[1:],[0]]) + np.hstack([numbers[2:],[0,0]])
print(larger_than_prev(numbers[:-2]))
