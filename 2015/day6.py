
lines = open('input/inputDay6.txt', 'r')

def getPoints(line):
    splitted = line.rstrip().split(' ')
    x2 = int(splitted[-1].split(',')[0])
    y2 = int(splitted[-1].split(',')[1])
    x1 = int(splitted[-3].split(',')[0])
    y1 = int(splitted[-3].split(',')[1])
    return (x1,y1,x2,y2)

## Part 1
gridSize = 1000
grid = [[0 for _ in range (gridSize)] for _ in range(gridSize)]

def updateGridV1(grid, line):
    (x1,y1,x2,y2) = getPoints(line)
    if "on" in line:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x][y] = 1
    elif "off" in line:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x][y] = 0
    else:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x][y] = int(not(grid[x][y]))
    return grid

for line in lines:
    grid = updateGridV1(grid,line)
    
result = sum(map(sum, grid))
print(result)

## Part 2
lines.seek(0)
gridSize = 1000
grid = [[0 for _ in range (gridSize)] for _ in range(gridSize)]

def updateGridV2(grid, line):
    (x1,y1,x2,y2) = getPoints(line)
    if "on" in line:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x][y] += 1
    elif "off" in line:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x][y] = max(0, grid[x][y] - 1)
    else:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                grid[x][y] += 2
    return grid

for line in lines:
    grid = updateGridV2(grid,line)

result = sum(map(sum, grid))
print(result)

lines.close()
