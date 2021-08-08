# сортировка словаря
dict = {'Usa': 'Washington', 'Russia':'Moscow', 'Spain':'Madrid'}
print(dict)

my_sorted = sorted(dict)
print(my_sorted)

my_sorted = sorted(dict.keys())
print(my_sorted)

my_sorted = sorted(dict.values())
print(my_sorted)

my_sorted = sorted(dict.items())
print(my_sorted)


population = {"Shanghai": 24256800, "Karachi": 23500000, "Beijing": 21516000, "Delhi": 16787941}
population_sorted = sorted(population.items(), key=lambda x: x[1])
print(population_sorted)