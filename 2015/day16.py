
sues = open('input/inputDay16.txt', 'r')

def property_to_tuple(property):
    return (property.split(': ')[0], int(property.split(': ')[1]))

sues_dict = {}
for sue in sues:
    name = sue.split(':')[0].strip()
    properties = sue.lstrip(name + ': ').strip().split(', ')
    properties = [property_to_tuple(property) for property in properties]
    sues_dict[name] = properties

sues.close()

properties = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3), ('akitas', 0),
              ('vizslas', 0), ('goldfish', 5), ('trees', 3), ('cars', 2), ('perfumes', 1)]

## Part 1
match = {}
for sue in sues_dict:
    properties_match = 0
    for property in sues_dict[sue]:
        if property in properties:
            properties_match += 1
    match[sue] = properties_match

print(max(match, key=match.get))


## Part 2
def get_property(name):
    for property in properties:
        if property[0] == name:
            return property
    return Warning('No such property')

match = {}
for sue in sues_dict:
    properties_match = 0
    for property in sues_dict[sue]:
        if property[0] == 'cats' or property[0] == 'trees':
            if property[1] > get_property(property[0])[1]:
                properties_match += 1
        elif property[0] == 'pomeranians' or property[0] == 'goldfish':
            if property[1] < get_property(property[0])[1]:
                properties_match += 1
        elif property in properties:
            properties_match += 1
    match[sue] = properties_match

print(max(match, key=match.get))
