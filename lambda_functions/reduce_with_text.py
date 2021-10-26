from functools import reduce

names = ["Monica", "Jack", "Tina", "John"]
total = reduce(lambda x, y: x + y[:2], names, '')
print(total)