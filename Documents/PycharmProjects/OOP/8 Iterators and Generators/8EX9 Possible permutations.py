from itertools import permutations

def possible_permutations(my_list):
    permutations_list = permutations(my_list)
    for perm in permutations_list:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
