
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
            if len(splitted_molecule) > 1: # If key is present in molecule
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
'''
# Alternative is to swap the replacements and do the search top-down

#molecule = 'HSiAl'
# Iterative depth-first with loop detection
# Alternatief: binary search in functie van max_depth om zo de under bound van het aantal stappen (de depth) te vinden
max_depth = 350
queue = [{'e'}]
while molecule not in set.union(*queue) and max_depth < len(molecule): #len(molecule):
    max_depth += 1
    print(max_depth)
    depth = 0
    queue = [{'e'}]
    examined = set()
    while queue != [] and molecule not in set.union(*queue):
        if depth == max_depth:
            del queue[0]
            depth -= 1
        else:
            el = queue[0].pop()
            #print(el)
            if el not in examined:
                molecules = build_molecules(set([el]), replacements)
                queue.insert(0, molecules)
                depth += 1
                examined.add(el)
        if set() in queue:
            queue.remove(set())
        #print(queue)
        #print('depth', depth, 'max_depth', max_depth)
    queue.append(set())
print('Found', max_depth)


#molecule = 'HSiAl'
'''
max_depth = 0
queue = [{'e'}]
prev_depth_queue = {'e'}
while molecule not in set.union(*queue) and max_depth < len(molecule):
    max_depth += 1
    print(max_depth)
    depth = max_depth - 1
    queue = [prev_depth_queue]
    prev_depth_queue = set()
    while queue != [] and molecule not in set.union(*queue):
        if depth == max_depth:
            prev_depth_queue = prev_depth_queue.union(queue[0])
            del queue[0]
            depth -= 1
        else:
            el = queue[0].pop()
            #print(el)
            molecules = build_molecules(set([el]), replacements)
            queue.insert(0, molecules)
            depth += 1
        if set() in queue:
            queue.remove(set())
        #print(queue)
        #print('depth', depth, 'max_depth', max_depth)
    queue.append(set())
print('Found', max_depth)
'''

 
import sys
import random
import re

repls = list()
m = ''
for line in sys.stdin:
    line = line.strip()
    try:
        cs, repl = line.split(' => ')
        repls.append((cs,repl))
    except ValueError:
        if line: m = line
n = set()
for r in repls:
    for match in re.finditer(r[0], m):
        s,e = match.span()
        n.add(m[:s] + r[1] + m[e:])
print('Total number of possible molecules after 1 replacement:', len(n))

def replace(st, i):
    if st == 'e': return i
    for r in repls:
        match = re.search(r[1], st)
        if match:
            s,e = match.span()
            return replace(st[:s] + r[0] + st[e:], i + 1)

searching = True
while searching:
    i = replace(m, 0)
    if i:
        print('Minimum number of replacement required:', i)
        searching = False
    else:
        random.shuffle(repls)