lst = [1, 2, 4, 5, 32]


def square(x):
    return x * x


print(map(square, lst))
print(list(map(square, lst)))


square_lst = []
for elem in lst:
    square_lst.append(elem * elem)

print(square_lst)

# pythonic way to do this is using list comprehensions
new_lst = [square(elem) for elem in lst]
print(new_lst)