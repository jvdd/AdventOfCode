
lines = open('input/inputDay08.txt', 'r')

## Part 1
nbCharactersRepresentation = 0
nbCharactersInMemory = 0
for line in lines:
	nbCharactersRepresentation += len(line.rstrip())
	nbCharactersInMemory += len(eval(line))

difference = nbCharactersRepresentation - nbCharactersInMemory
print(difference)

## Part 2
lines.seek(0)
difference = 0
for line in lines:
	difference += 2 + line.rstrip().count('\"') + line.rstrip().count('\\')

print(difference)

lines.close()
