
textfile = open("inputDay5.txt",'r')

## Part 1
vowels = "aeiou"
notAllowedParts = ["ab", "cd", "pq", "xy"]

nice = 0
for string in textfile:
	if not any(part in string for part in notAllowedParts):
		nbVowels = 0
		doubleOk = False
		prevChar = []
		for char in string:
			if char in vowels:
				nbVowels += 1
			if not doubleOk:
				if prevChar == char:
					doubleOk = True
				else:
					prevChar = char
		if nbVowels >= 3 and doubleOk:
			nice += 1

print(nice)

## Part 2
textfile.seek(0) # Set the UNIX read-write pointer back to the beginning
nice = 0
for string in textfile:
	repeat2Ok = False
	repeat1Ok = False
	for i in range(len(string)-3):
		char = string[i]
		if char + string[i+1] in string[i+2:]: # Does not matter that this only is checked untill length - 3, since in last 3 characters it cannot ocuur anymore
			repeat2Ok = True
		if char == string[i+2]:
			repeat1Ok = True
	if repeat2Ok and repeat1Ok:
		nice += 1

print(nice)


textfile.close()

# NOTE
# There might be a way more beautiful solution by using regex
# but implementing the problem in this way, was quite fast, and
# this solution is not that ineficient.