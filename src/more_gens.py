lst = [-1, -2, -3, 1, 2, 3, 0, 10, -5]

# генератор списка
l = [i for i in lst]
print(l)

# генератор множества
my_set = {i for i in lst}
print(my_set)

# генератор словаря
my_dict_a = {i:i for i in lst}
my_dict_b = {i:i**2 for i in lst}
print(my_dict_a)
print(my_dict_b)

# генератор строки
# для создания строки используется метод join, которому передается генератор
# не забываем что join принимает только строки в качестве аргумента
print(",".join(str(i) for i in lst))