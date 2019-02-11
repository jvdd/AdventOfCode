# Sorry if this is considered cheating
from hashlib import md5

# Function used for both parts
def findValidHash(key, nbZeros):
	number = 0
	valid = False
	while not valid:
		number += 1
		m = md5() # idk if this is cheating or not :p (saved me a lot of time though)
		m.update(key + str(number))
		valid = m.hexdigest()[0:nbZeros] == '0'*nbZeros
	return (number,m.hexdigest())


## Part 1
key = "bgvyzdsv"
nbZeros = 5
(number,hexHash) = findValidHash(key,nbZeros)
print(str(number) + " " + str(hexHash))


## Part 2
key = "bgvyzdsv"
nbZeros = 6
(number,hexHash) = findValidHash(key,nbZeros)
print(str(number) + " " + str(hexHash))
