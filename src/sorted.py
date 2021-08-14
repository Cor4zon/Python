from random import shuffle

my_list = [1, 2, 3, 4, 5, 6, 7]
shuffle(my_list)
print(my_list)
my_list_sorted = sorted(my_list)
print(my_list)

my_set = {1, 4, 2, 7, 33, 1, 3}
my_set_sorted = sorted(my_set, reverse=True)
print(my_set_sorted)

# использование параметра key
my_files = ['somecat.jpg', 'pc.png', 'apple.bmp', 'mydog.gif']
my_files_sorted = sorted(my_files, key=len)
print(my_files_sorted)
