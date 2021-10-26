lst = list(range(1, 21))

isThereEven = list(map(lambda x: x % 2 == 0, lst))
print(isThereEven)
print(any(isThereEven))