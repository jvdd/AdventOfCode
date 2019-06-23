
from itertools import combinations_with_replacement, permutations

ingredients = open('input/inputDay15.txt', 'r')

ingredients_dict = {}
for ingredient in ingredients:
    split_ingredients = ingredient.split(':')
    name = split_ingredients[0].strip()
    points = list(map(int, split_ingredients[1].replace(',','').strip().split(' ')[1::2]))
    ingredients_dict[name] = points

ingredients.close()

teaspoons = 100

## Part 1
combinations = []
for combination in combinations_with_replacement(range(0, teaspoons+1), 4):
    if sum(combination) == teaspoons:
        combinations.append(combination)

def getTotalScore1(ingredients, combination):
    capacity, durability, flavour, texture = 0, 0, 0, 0
    for n in range(0, len(combination)):
        capacity += ingredients_dict[ingredients[n]][0] * combination[n]
        durability += ingredients_dict[ingredients[n]][1] * combination[n]
        flavour += ingredients_dict[ingredients[n]][2] * combination[n]
        texture += ingredients_dict[ingredients[n]][3] * combination[n]

    if capacity < 1 or durability < 1 or flavour < 1 or texture < 1:
        return 0
    else:
        return capacity * durability * flavour * texture

max_result = 0
for each in permutations(ingredients_dict, 4):
    for n in combinations:
        result = getTotalScore1(each, n)
        if result > max_result:
            max_result = result

print(max_result)


## Part 2
def getTotalScore2(ingredients, combination):
    capacity, durability, flavour, texture, calorie = 0, 0, 0, 0, 0
    for n in range(0, len(combination)):
        capacity += ingredients_dict[ingredients[n]][0] * combination[n]
        durability += ingredients_dict[ingredients[n]][1] * combination[n]
        flavour += ingredients_dict[ingredients[n]][2] * combination[n]
        texture += ingredients_dict[ingredients[n]][3] * combination[n]
        calorie += ingredients_dict[ingredients[n]][4] * combination[n]

    if calorie != 500 or capacity < 1 or durability < 1 or flavour < 1 or texture < 1:
        return 0
    else:
        return capacity * durability * flavour * texture

max_result = 0
for permutation in permutations(ingredients_dict, 4):
    for combination in combinations:
        result = getTotalScore2(permutation, combination)
        if result > max_result:
            max_result = result

print(max_result)