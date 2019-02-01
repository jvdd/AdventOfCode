
sequence = "1113222113"

def nextSequence(sequence):
	nextSeq = ""
	index = 0
	while index < len(sequence):
		el = sequence[index]
		nextEls = ""
		i = index + 1
		while i < len(sequence) and sequence[i] == el:
			nextEls += sequence[i]
			i += 1
		if len(nextEls) > 0:
			nextSeq += str(len(nextEls) + 1) + el
			index += len(nextEls)
		else:
			nextSeq += "1" + el
		index += 1

	return nextSeq

## Part 1
for i in range(40):
	sequence = nextSequence(sequence)

print(len(sequence))


## Part 2
for i in range(10):
	sequence = nextSequence(sequence)

print(len(sequence))