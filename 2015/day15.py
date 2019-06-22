from itertools import combinations_with_replacement, permutations

ingredients = open('input/inputDay15.txt', 'r')

ingredients_dict = {}
for ingredient in ingredients:
    split_ingredients = ingredient.split(':')
    name = split_ingredients[0]
    points = list(map(int, split_ingredients[1].replace(',','').strip().split(' ')[1::2]))
    ingredients_dict[name] = points

ingredients.close()

teaspoons = 100


## Part 1
combinations = []
for each in combinations_with_replacement(range(1, 98), 4):
    if sum(each) == teaspoons:
        combinations.append(each)

def getTotal1(components, numbers):
    capacity, durability, flavour, texture = 0, 0, 0, 0
    for n in range(0, len(numbers)):
        capacity += ingredients_dict[components[n]][0] * numbers[n]
        durability += ingredients_dict[components[n]][1] * numbers[n]
        flavour += ingredients_dict[components[n]][2] * numbers[n]
        texture += ingredients_dict[components[n]][3] * numbers[n]

    if capacity < 1 or durability < 1 or flavour < 1 or texture < 1:
        return 0
    else:
        return capacity * durability * flavour * texture

max_result = 0
for each in permutations(ingredients_dict, 4):
    for n in combinations:
        result = getTotal1(each, n)
        if result > max_result:
            max_result = result

print(max_result)


## Part 2
def getTotal2(components, numbers):
    capacity, durability, flavour, texture, calorie = 0, 0, 0, 0, 0
    for n in range(0, len(numbers)):
        capacity += ingredients_dict[components[n]][0] * numbers[n]
        durability += ingredients_dict[components[n]][1] * numbers[n]
        flavour += ingredients_dict[components[n]][2] * numbers[n]
        texture += ingredients_dict[components[n]][3] * numbers[n]
        calorie += ingredients_dict[components[n]][4] * numbers[n]

    if calorie != 500 or capacity < 1 or durability < 1 or flavour < 1 or texture < 1:
        return 0
    else:
        return capacity * durability * flavour * texture

max_result = 0
for each in permutations(ingredients_dict, 4):
    for n in combinations:
        result = getTotal2(each, n)
        if result > max_result:
            max_result = result

print(max_result)