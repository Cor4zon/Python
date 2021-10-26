"""Filtering a list of numbers 1"""
lst = list(range(1, 21))

evens = list(filter(lambda x: x % 2 == 0, lst))
odds = list(filter(lambda x: x % 2 != 0, lst))

print(lst)
print(evens)
print(odds)
