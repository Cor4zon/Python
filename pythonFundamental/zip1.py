
lst1 = ['a', 'b', 'c']
lst2 = [11, 21, 44]
lst3 = [(1, 1), (2, 2), (3, 3)]

for count, (a, b, c) in enumerate(zip(lst1, lst2, lst3)):
    print(count, a, b, c)
