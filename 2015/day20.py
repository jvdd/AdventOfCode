
nb_presents = 29000000

from functools import reduce

# Source: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):  
    res_set = set([1, n])
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: 
            res_set.add(i)
            res_set.add(n//i)
    return res_set

## Part 1
house_number = 0
curren_nb_presents = 0
while curren_nb_presents < nb_presents:
    house_number += 1
    facs = factors(house_number)
    curren_nb_presents = sum(list(map(lambda x : 10 * x, facs)))

print(house_number)


## Part 2
facs_dict = {}
visit_limit = 50
house_number = 0
curren_nb_presents = 0
while curren_nb_presents < nb_presents:
    house_number += 1
    facs = factors(house_number)
    remove_facs = set()
    for fac in facs:
        if fac in facs_dict.keys():
            if facs_dict[fac] == 50:
                remove_facs.add(fac)
            else:
                facs_dict[fac] += 1
        else:
            facs_dict[fac] = 1
    facs = facs.difference(remove_facs)
    curren_nb_presents = sum(list(map(lambda x : 11 * x, facs)))

print(house_number)