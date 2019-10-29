
from dataclasses import dataclass
from constraint import *
import math

@dataclass
class Item: # Represents a weapon, armor or ring
    sort : str # Weapons, Armor, Rings
    name : str 
    cost : int 
    damage : int
    armor : int

my_hit_points = 100
f = open('input/inputDay21.txt')
f.readline() # Skip first line
boss_stats = {}
for i in range(3):
    line_split = f.readline().split(': ')
    boss_stats[line_split[0]] = int(line_split[1])
f.readable(), f.readline(), f.readline() # Skip 3 lines
items = {}
for line in f:
    if line.rstrip() == '': # Skip empty line
        continue
    elif ':' in line:
        sort = line.split(':')[0]
        items[sort] = []
    else:
        line_split = line.split()
        line_split = [sort, line_split[0]] + list(map(int, line_split[1:]))
        item = Item(*line_split)
        items[sort].append(item)
f.close()

emptyArmor = Item('Armor', 'empty', 0, 0, 0)
emptyRing = Item('Rings', 'empty', 0, 0, 0)

def build_CLP_problem():
    problem = Problem()
    problem.addVariable("w", [item for item in items['Weapons']])
    problem.addVariable("a", [emptyArmor] + [item for item in items['Armor']])
    problem.addVariable('r1', [emptyRing] + [item for item in items['Rings']])
    problem.addVariable('r2', [emptyRing] + [item for item in items['Rings']])
    problem.addConstraint(lambda r1, r2 : (not r1 == emptyRing) or (r2 == emptyRing), ('r1', 'r2')) # if r1 == 0 => r2 == 0 ~ (p -> q = not p or q)
    problem.addConstraint(lambda r1, r2 : (not r1 != emptyRing) or (r2 != r1), ('r1', 'r2')) # if r1 != 0 => r2 != r1 ~ (p -> q = not p or q)
    return problem

def win_constraint(w, a, r1, r2):
    damage_to_boss = max(1, (w.damage + a.damage + r1.damage + r2.damage) - boss_stats['Armor']) 
    damage_to_player = max(1, boss_stats['Damage'] - (w.armor + a.armor + r1.armor + r2.armor))
    # HP - dmg*rounds = 0 -> rounds = ceil(HP / dmg)
    boss_rounds_to_0 = math.ceil(boss_stats['Hit Points'] / damage_to_boss)
    player_rounds_to_0 = math.ceil(my_hit_points / damage_to_player) 
    return boss_rounds_to_0 <= player_rounds_to_0

## Part 1
problem = build_CLP_problem()
problem.addConstraint(win_constraint, ('w', 'a', 'r1', 'r2'))
options = problem.getSolutions()
print(min([sum([option[key].cost for key in option.keys()]) for option in options]))

## Part 2
problem = build_CLP_problem()
problem.addConstraint(lambda w, a, r1, r2 : not win_constraint(w, a, r1, r2), ('w', 'a', 'r1', 'r2'))
options = problem.getSolutions()
print(max([sum([option[key].cost for key in option.keys()]) for option in options]))
