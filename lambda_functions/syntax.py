"""
def sum(a, b, c):
    sum = a + b + c
    return sum

lambda a, b, c: a + b + c
"""

def second(lst):
    return lst[1]

a = [(1, 1), (-3, 5), (4, 0), (2, 2)]
print(a)
a.sort(key=second)
print(a)

# best way
a.sort(key=lambda a: a[1])
print(a)

