
import re

alphabet = "abcdefghijklmnopqrstuvwxyz"
def valid(password):
	doubles = re.findall(r'((\w)\2)', password)
	if len(doubles) >= 2 and any(double != doubles[0] for double in doubles[1:]):
		if not any(el in password for el in "iol"): # Could be improved by shifting over those
			if any(alphabet[i:i+3] in password for i in range(len(alphabet) - 2)):
				return True
	return False

def nextPassword(password):
	pos = len(password) - 1
	while not valid(password):
		if password[pos] == "z":
			pos = pos -1
		else:
			password = password[:pos] + chr(ord(password[pos]) + 1) + password[pos+1:]
			if pos < len(password)-1:
				password = password[:pos+1] + "a"*(len(password) -1 - pos)
				pos = len(password) - 1
	
	return password

## Part 1
password = "vzbxkghb"
result = nextPassword(password)
print(result)


## Part 2
def increment(string):
	pos = len(string) - 1
	while string[pos] == "z":
		pos -= 1
	string = string[:pos] + chr(ord(string[pos]) + 1) + string[pos+1:]
	if pos < len(password)-1:
		string = string[:pos+1] + "a"*(len(string) -1 - pos)
	
	return string

password = increment(result)
result = nextPassword(password)
print(result)


# NOTE
# I could use the increment function in the nextPassword() method
# but this would be at the cost of some (minor) efficiency.
# Hence, I opted to only use this method to increment the previous
# result in the 2nd part of the challenge.
