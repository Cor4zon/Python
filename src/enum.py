#enumerate

lst = ['metallica', 'megadeth', 'slayer', 'anthrax']
print(list(enumerate(lst)))
for i, element in enumerate(lst):
    print(i, element)