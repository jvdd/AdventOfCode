
circuit = ["123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h", "NOT y -> i"]

## Part 1
notDict = {}
andDict = {}
orDict = {}
lshiftDict = {}
rshiftDict = {}
varDict = {}

for line in circuit:
	splittedLine = line.rstrip().split['->']
	if "NOT" in line:
		notDict[splittedLine[0].split(' ')[1]] = splittedLine[1]
	elif "AND" in line or "OR" in line or "LSHIFT" in line or "RSHIFT" in line:
		(x,y) = (splittedLine[0].split(' ')[0],splittedLine[0].split(' ')[2])
		if "AND" in line:
			andDict[(x,y)] = splittedLine[1]
		elif "OR" in line:
			orDict[(x,y)] = splittedLine[1]
		elif "LSHIFT" in line:
			lshiftDict[(x,y)] = splittedLine[1]
		elif "RSHIFT" in line:
			rshiftDict[(x,y)] = splittedLine[1]
	else:
		varDict[splittedLine[1]] = int(splittedLine[0])


def completeVars():
	dicts = [notDict, andDict, orDict, lshiftDict, rshiftDict]

# Recursief rule finding algo die dat dan toepast zou chaud zijn
def findRulesElements(el):


def find(var):
	toFind = [var]
	while len(toFind) > 0:
		newToFind = []
		for el in toFind:
			if el not in varDict:
				newToFind += findRulesElements(el)
		toFind = newToFind
	
	return varDict(var)

find("a")