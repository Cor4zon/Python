from functools import reduce

lst = list(range(1, 11))

total = reduce(lambda x, y: x + y, lst)
print(total)

# equal
print(sum(lst))