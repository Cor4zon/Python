names = ["a b", "a a", "j w", "k m", "l e"]

names.sort()
print(names)

names.sort(key=lambda x: x.split()[-1])
print(names)