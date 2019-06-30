
replacements_molecule = open('input/inputDay19.txt', 'r')

replacements = []
final = False
for line in replacements_molecule:
    if final:
        molecule = line.strip()
    if not final and line.strip() != '':
        splitted_replacement = line.strip().split(' => ')
        replacements.append((splitted_replacement[0], splitted_replacement[1]))
    else:
        final = True
    
replacements_molecule.close()

## Part 1
def create_molecule(splitted_molecule, i, key, value):
    add_key = lambda x : x + key 
    add_value = lambda x : x + value
    result = ''
    for j, split in enumerate(splitted_molecule[:-1]):
        if i == j:
            result += add_value(split)
        else:
            result += add_key(split)
    result += splitted_molecule[-1]
    return result

# search 1 depth and return molecules at next depth
def build_molecules(start_molecules, replacements):
    molecules = set()
    for molecule in start_molecules:
        for replacement in replacements:
            key, value = replacement
            splitted_molecule = molecule.split(key)
            if len(splitted_molecule) > 1:
                for i in range(len(splitted_molecule)-1):
                    replaced = create_molecule(splitted_molecule, i, key, value)
                    molecules.add(replaced)
    return molecules

start_molecules = set([molecule])
print(len(build_molecules(start_molecules, replacements)))


## Part 2
# THIS WORKS TOO SLOW (this does the search bottom up)
'''
molecules = set(['e'])
step = 0
while molecule not in molecules:
    molecules = build_molecules(molecules, replacements)
    step += 1
    print(step)
print(step)
'''

# Alternative is to swap the replacements and do the search top-down

def prune_molecules(molecules, size):
    result = set()
    for molecule in molecules:
        if len(molecule) < size:
            result.add(molecule)
    return result

replacements_swap = list(map(lambda t: (t[1], t[0]), replacements))
prune_size = len(molecule) - 2
molecules = set([molecule])
step = 0
while 'e' not in molecules:
    molecules = build_molecules(molecules, replacements_swap)
    molecules = prune_molecules(molecules, prune_size)
    step += 1
    prune_size -= 2
    print(step, len(molecules))
print(step)
