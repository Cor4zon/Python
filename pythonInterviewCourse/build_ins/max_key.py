from map_map import square

lst = [1, 2, -5, 4]

print(max(lst))

print(max(lst, key=square))

print(max(lst, key=lambda x: x * x))