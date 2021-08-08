# функция slice
person = ('John', 'Jones', 'May', 12, 2000)
NAME, BIRTH = slice(None, 2), slice(2, None)
print(person[NAME], person[BIRTH])

my_list = [1, 2, 3, 4, 5, 6, 7]
EVEN = slice(1, None, 2)
print(my_list[EVEN])

# изменение части последовательности с помощью срезов
my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
my_list[1:3] = [20, 30]
print(my_list)
my_list[1:4] = [0]  # важно: передаем итерируемый объект
print(my_list)
my_list[2:] = [6, 6, 7, 77]
print(my_list)


# также можно удалять часть последовательности
my_list[3:] = []
print(my_list)

