
distances = open('input/inputDay9.txt', 'r')

travelMap = {}
allCities = []
for distance in distances:
    splittedDistance = distance.rstrip().split(' ')
    (cityA, cityB) = (splittedDistance[0], splittedDistance[2]) # I assume that cities are always 1 name
    travelMap[(cityA, cityB)] = int(splittedDistance[-1])
    if cityA not in allCities:
        allCities += [cityA]
    if cityB not in allCities:
        allCities += [cityB]

distances.close()

def permute(list, acc=[], res=[]):
    if len(list) == 1:
        res += [acc + list]
    for i in range(len(list)):
        permute(list[:i] + list[i+1:], acc + [list[i]], res)
    return res

def getDistance(cityA, cityB):
    if (cityA,cityB) in travelMap:
        return travelMap[(cityA, cityB)]
    elif (cityB, cityA) in travelMap:
        return travelMap[(cityB, cityA)]
    else:
        Exception('Santa can\'t travel to these cities')

def length(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += getDistance(path[i],path[i+1])
    return dist


## Part 1
paths = permute(allCities)
minDist = length(paths[0])
for i in range(1,len(paths)):
    dist = length(paths[i])
    if dist < minDist:
        minDist = dist

print(minDist)


## Part 2
maxDist = length(paths[0])
for i in range(1,len(paths)):
    dist = length(paths[i])
    if dist > maxDist:
        maxDist = dist

print(maxDist)

# NOTE
# It is not necessary to look at all the permutations,
# some directed search would be more optimal.
# But this is for sure one of the more fast approaches
# in regards of development time.
