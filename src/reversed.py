# функция reversed
my_files = ['somecat.jpg', 'pc.png', 'apple.bmp', 'mydog.gif']
print(my_files)
# print(my_files.reverse())
reversed_list = reversed(my_files)
print(my_files)
print(reversed_list)
print(list(reversed_list))



# у списка и только у списка есть два метода sort и reverse.
# меняют сам список, а не его копию
print("SORT & REVERSE METHODS ONLY FOR LISTS")
print(my_files)
my_files.reverse()
print("reverse:")
print(my_files)
my_files.sort()
print('sort:')
print(my_files)