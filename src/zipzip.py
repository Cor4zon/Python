

keys = ['a', 'b', 'c', 'd']
lst = [1, 2, 3]


print(list(zip(keys, lst)))
dic = dict(zip(keys, lst))
print(dic)


for key, num in zip(keys, lst):
    print(key, num)


a = [1, 2, 3, 4, 5]
b = ('y', 'x', 'z', 'b', 'a')
c = [5, 5, 5, 5, 5, 5, 5, 5, 5]

print(list(zip(a, b, c)))
print(type(zip(a, b, c)))

from itertools import zip_longest
print(list(zip_longest(a, b, c)))


s = (1, 2, 3, 4, 5)
t = ['a', 'b' , 'c', 'd', 'e']

def my_zip(s, t):
    return [(s[i], t[i]) for i in range(len(s))]

print(my_zip(s, t))