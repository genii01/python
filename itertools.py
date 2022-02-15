from itertools import permutations, combinations, product

items = [1,2,3]
print(list(combinations(items,2)))

items= [[1,2,3],[5,6]]
print(list(product(*items)))