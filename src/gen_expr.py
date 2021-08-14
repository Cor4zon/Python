# генераторы выражений
list_a = [1, 2, 4, -4, 0, 0, -12, -17, 5, 7, 7, 666, -142]
my_gen = (i for i in list_a)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


lst = [1, 2, 3, 4]

my_gen = (i for i in lst)

print(sum(my_gen)) #10

print(sum(my_gen)) #0