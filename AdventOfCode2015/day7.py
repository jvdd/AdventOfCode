
circuit = ["123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h", "NOT y -> i"]

## Part 1
'''
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
	return dicts

# Recursief rule finding algo die dat dan toepast zou chaud zijn
def findRulesElements(el):
	dicts = completeVars()
	for subdict in dicts:
		for key, value in subdict.items():
			if value == el:
				

def find(var):
	toFind = [var]
	while len(toFind) > 0:
		newToFind = []
		for el in toFind:
			if el not in varDict:
				newToFind += findRulesElements(el)
		toFind = newToFind
	
	return varDict[var]
'''

varDict = {}

def findRule(var):
	for rule in circuit:
		if rule.rstrip().split(' ')[-1] == var:
			return rule

# TODO fix overflow en underflow in 16-bits
def find(var):
	if var in varDict:
		return varDict[var]
	if var is int:
		return var # Makes RSHIFT and LSHIFT work
	rule = findRule(var)
	print(rule)
	splittedRule = rule.rstrip().split('->')
	if "NOT" in rule:
		return ~ find(splittedRule[0].split(' ')[1])
	elif "AND" in rule or "OR" in rule or "LSHIFT" in rule or "RSHIFT" in rule:
		(x,y) = (splittedRule[0].split(' ')[0],splittedRule[0].split(' ')[2])
		if "AND" in rule:
			binaryOperator = lambda x, y : x & y
		elif "OR" in rule:
			binaryOperator = lambda x, y : x | y
		elif "LSHIFT" in rule:
			binaryOperator = lambda x, y : x << y
			return find(x) 
		elif "RSHIFT" in rule:
			binaryOperator = lambda x, y : x >> y
		return binaryOperator(find(x), find(y))
	else:
		varDict[var] = int(splittedRule[0])
		return varDict[var]

print(find("i"))