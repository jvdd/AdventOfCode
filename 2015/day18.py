
import numpy as np

gridSize = 100
initial_grid = np.zeros((gridSize,gridSize))

initial_config = open('input/inputDay18.txt', 'r')

def get_config(token):
    if token == '#':
        return 1
    elif token == '.':
        return 0
    raise ValueError('Invalid token: ' + token)

for i, line in enumerate(initial_config):
    for j in range(gridSize):
        initial_grid[i,j] = get_config(line[j])

initial_config.close()

## Part 1
steps = 100

# Extra function used for debugging
def print_grid(grid):
    for line in grid:
        string = []
        for char in line:
            if char == 1: string.append('#')
            else: string.append('.')
        print(string)
    print('---------------------------------')

def get_neighbors(grid, i , j, gridSize):
    neighbors = []
    if i > 0: 
        neighbors.append(grid[i-1,j])
        if j > 0: neighbors.append(grid[i-1,j-1])
        if j < gridSize-1: neighbors.append(grid[i-1,j+1])
    if i < gridSize-1: 
        neighbors.append(grid[i+1,j])
        if j > 0: neighbors.append(grid[i+1,j-1])
        if j < gridSize-1: neighbors.append(grid[i+1,j+1])
    if j > 0: neighbors.append(grid[i,j-1])
    if j < gridSize-1: neighbors.append(grid[i,j+1])
    
    if len(neighbors) < 8:
        neighbors += [0] * (8 - len(neighbors))

    return neighbors

grid = initial_grid.copy()
for _ in range(steps):
    new_grid = np.zeros((gridSize,gridSize))
    for i in range(gridSize):
        for j in range(gridSize):
            neighbors = get_neighbors(grid, i , j, gridSize)
            if grid[i,j] == 1 and sum(neighbors) in [2,3]:
                new_grid[i,j] = 1
            if grid[i,j] == 0 and sum(neighbors) == 3:
                new_grid[i,j] = 1
    grid = new_grid

print(int(sum(sum(grid))))


## Part 2
steps = 100

grid = initial_grid.copy()
grid[0,0] = 1
grid[0,gridSize-1] = 1
grid[gridSize-1,0] = 1
grid[gridSize-1,gridSize-1] = 1
for _ in range(steps):
    new_grid = np.zeros((gridSize,gridSize))
    for i in range(gridSize):
        for j in range(gridSize):
            if i in [0,gridSize-1] and j in [0,gridSize-1]:
                new_grid[i,j] = 1
            else:
                neighbors = get_neighbors(grid, i , j, gridSize)
                if grid[i,j] == 1 and sum(neighbors) in [2,3]:
                    new_grid[i,j] = 1
                if grid[i,j] == 0 and sum(neighbors) == 3:
                    new_grid[i,j] = 1
    grid = new_grid

print(int(sum(sum(grid))))
