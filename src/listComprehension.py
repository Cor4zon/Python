
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

# more Pythonic than loops
# more declarative than loop (easier to read)
lst = [i * i for i in range(10)]
print(lst)

def get_square(x):
    return x * x

map_list = list(map(get_square, list(range(10))))
print(map_list)


last_way = [get_square(i) for i in range(10)]
print(last_way)

last_way.sort(reverse=True)
print(last_way)
last_way.sort()
print(last_way)

print(sorted(map_list, reverse=True))

d = {'x': 1, 'b':2, 'z':3}
print(d)
print(d.values())
print(d.keys())
print(d.items())

a = [1, 2, 3]
b = [4, 5]
# из звездного питона
c = [*a, *b]
print(c)

c = ['a', 'b', 'c', 'd']

d2 = dict(zip(c, a))
print(d2)

d3 = {**d, **d2}
print(d3)


# еще можно copy + update