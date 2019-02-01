
lines = open('input/inputDay7.txt', 'r')

circuit = []
for rule in lines:
	circuit += [rule]

lines.close()

## Part 1
varDict = {}

def findRule(var):
	for rule in circuit:
		if rule.rstrip().split(' ')[-1] == var:
			return rule

# https://wiki.python.org/moin/BitwiseOperators
def find(var):
	if var in varDict:
		return varDict[var]
	try:
		var = int(var) # Makes RSHIFT and LSHIFT work
		return var
	except ValueError:
		pass
	rule = findRule(var)	
	splittedRule = rule.rstrip().split('->')
	if "NOT" in rule:
		varDict[var] = ~ find(splittedRule[0].split(' ')[1])
	elif "AND" in rule or "OR" in rule or "LSHIFT" in rule or "RSHIFT" in rule:
		(x,y) = (splittedRule[0].split(' ')[0],splittedRule[0].split(' ')[2])
		if "AND" in rule:
			binaryOperator = lambda x, y : x & y
		elif "OR" in rule:
			binaryOperator = lambda x, y : x | y
		elif "LSHIFT" in rule:
			binaryOperator = lambda x, y : x << y
		elif "RSHIFT" in rule:
			binaryOperator = lambda x, y : x >> y
		varDict[var] = binaryOperator(find(x), find(y))
	else:
		try:
			value = int(splittedRule[0])
			varDict[var] = value
		except ValueError:
			varDict[var] = find(splittedRule[0].strip())
	return varDict[var]
			
print(find('a') % 65536) # Because we work in 16-bit representation


## Part 2
def override(circuit, value, var):
	rule = findRule(var)
	circuit.remove(rule)
	circuit += [str(value) + " -> " + var]
	return circuit

circuit = override(circuit, find('a'), 'b')

varDict = {}
print(find('a') % 65536) # Because we work in 16-bit representation


# NOTE
# I only performed the modulo operation in the end, to avoid the overhead of running
# this operation on each variable in the recursive function.
# This results in the same output, and since my computer does not work in 16-bit 
# representation it is not necessary to perform all operations on 16-bit numbers.
