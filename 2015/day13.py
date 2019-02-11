
sittingInfo = open('input/inputDay13.txt', 'r')

people = []
sittingMap = {}
for sitting in sittingInfo:
    splittedSitting = sitting.rstrip(".\n").split()
    (personA, personB) = (splittedSitting[0], splittedSitting[-1])
    value = int(splittedSitting[3])
    if splittedSitting[2] == "lose":
        value = -value
    sittingMap[(personA, personB)] = value
    if personA not in people:
        people += [personA]
    if personB not in people:
        people += [personB]

sittingInfo.close()

def permute(list, acc=[], res=[]):
    if len(list) == 1:
        res += [acc + list]
    for i in range(len(list)):
        permute(list[:i] + list[i+1:], acc + [list[i]], res)
    return res

def getHappiness(personA, personB):
    result = sittingMap[(personA, personB)]
    result += sittingMap[(personB, personA)]
    return result

def happiness(sitting):
    happiness = 0
    for i in range(len(sitting) - 1):
        happiness += getHappiness(sitting[i],sitting[i+1])
    happiness += getHappiness(sitting[0], sitting[-1])
    return happiness

## Part 1
sittings = permute(people[1:])
completeSitting = lambda y : [people[0]] + y
sittings = map(completeSitting, sittings)
maxHappiness = happiness(sittings[0])
for i in range(1,len(sittings)):
    happy = happiness(sittings[i])
    if happy > maxHappiness:
        maxHappiness = happy

print(maxHappiness)


## Part 2
sittings = permute(people)
maxHappiness = happiness(sittings[0]) - getHappiness(sittings[0][0], sittings[0][-1])
for i in range(1,len(sittings)):
    happy = happiness(sittings[i]) - getHappiness(sittings[i][0], sittings[i][-1])
    if happy > maxHappiness:
        maxHappiness = happy

print(maxHappiness)

# NOTE
# In part 2 I put myself at the first position in the permutation, 
# since my happiness is 0 for whoever is my neighbour, I substract
# the happiness values of the first and last person, so that this
# represents the 0 value of my position.
