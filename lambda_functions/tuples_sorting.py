people = [('Jack', 29), ('Ben', 10), ('Kate', 20), ('Victor', 22), ('Olga', 41)]

print(people)
people.sort()
print(people)

people.sort(key=lambda x: x[1])
print(people)

