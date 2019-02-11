
import re

book = open('input/inputDay12.txt', 'r')

## Part 1
total = 0
for line in book:
	numbers = re.findall(r'-?\d+', line)
	total += sum(map(int, numbers))

print(total)


## Part 2
book.seek(0)
wrong = 0
counter = 0
for line in book:
	counter += 1
	print(len(line))
	wrongParts = re.findall(r'{.*red.*}', line)
	print(len(wrongParts[0]))
	wrongNumbers = [re.findall(r'-?\d+', part) for part in wrongParts]
	wrong += sum(map(int, wrongNumbers[0]))

total = total - wrong
print(total)
print(counter)

book.close()