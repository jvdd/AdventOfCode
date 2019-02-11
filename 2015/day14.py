
import numpy as np

stats = open('input/inputDay14.txt', 'r')

reindeerStats = {}
for line in stats:
    splittedStats = line.split()
    reindeerStats[splittedStats[0]] = (int(splittedStats[3]), int(splittedStats[6]), int(splittedStats[-2]))

stats.close()

def distance(reindeer, time):
    (speed,runtime,resttime) = reindeerStats[reindeer]
    t = 0
    dist = 0
    while t < time:
        dist += speed * min(runtime,time-t)
        t += runtime + resttime
    return dist

## Part 1
endTime = 2503
dist = lambda x : distance(x, endTime)
maxDist = max(map(dist, reindeerStats.keys()))
print(maxDist)

## Part 2
def distanceVct(reindeer, time):
    (speed,runtime,resttime) = reindeerStats[reindeer]
    t = 0
    distVct = [0 for _ in range(time)]
    while t < time:
        distVct[t:t+min(runtime,time-t)] = [speed]*min(runtime,time-t)
        t += runtime + resttime
    return np.cumsum(distVct)

def points(time):
    reindeerPoints = {}
    for reindeer in reindeerStats.keys():
        reindeerPoints[reindeer] = distanceVct(reindeer, time)
    best = reindeerPoints.keys()[0]
    for i in range(time):
        for reindeer in reindeerPoints.keys():
            if reindeer != best and reindeerPoints[reindeer][i] > reindeerPoints[best][i]:
                best = reindeer
            reindeerPoints[reindeer][i] = 0
        reindeerPoints[reindeer][i] = 1
    
    sumPoints = lambda x : sum(reindeerPoints[x])
    return max(map(sumPoints, reindeerPoints.keys()))

result = points(endTime)
print(result)