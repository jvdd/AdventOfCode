
import re
import json

#book = open('input/inputDay12.txt', 'r')

with open('input/inputDay12.txt') as f:
	book = json.load(f)

## Part 1
numbers = re.findall(r'-?\d+', str(book))
total = sum(map(int, numbers))

print(total)


## Part 2
def item_sum(item):
	if isinstance(item, list):
		return sum([item_sum(i) for i in item])
	elif isinstance(item, dict):
		if 'red' in item.values():
			return 0
		return sum([item_sum(i) for i in item.values()])
	elif isinstance(item, int):
		return item
	else: # Return 0 for other items
		return 0

total = item_sum(book)

print(total)