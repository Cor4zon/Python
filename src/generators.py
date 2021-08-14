list_a = [2, 3, 5, 2, 5, 6, 1, 2, 3, -1, -2, -3, -4, -5]

# генератор только для четных элементов
list_b = [i for i in list_a if i % 2 == 0]
print(list_a)
print(list_b)

# несколько условий
list_c = [i for i in list_a if i % 2 == 0 and i > 0]
print(list_c)

# обработка элемента
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'bb', 'ccc', 'd']

# квадрат
list4 = [i**2 for i in list1]
print(list4)

# длина элемента
list5 = [len(i) for i in list2]
print(list5)

# генератор + тернарный оператор
list_of_pain = [1, -1, 2, -2, 5, -3, 88, -19]
list_of_happyness = [x if x > 0 else x**2 for x in list_of_pain]
print(list_of_happyness)

# внутри скобок можно переносить строки. это улучшает читаемость
llist = [
    i ** 2
    for i in list_of_pain
    if i > 0
]
print(llist)

