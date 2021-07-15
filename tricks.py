# 1. Объединение списков разной длины
L = [[1, 3, 4], [1, 2, 3], [4, 3], [4], [4, 2]]
lst1 = [1, 2, 3]
lst2 = [3, 4]
lst3 = [4]
lst4 = []
lst5 = [4, 5, 6, 6]

# вариант 1
print(lst1 + lst2 + lst3 + lst4 + lst5)

# вариант 2
print(sum(L, []))

# вариант 3
import itertools # сборник полезных итераторов

print(list(itertools.chain.from_iterable(L)))