from random import shuffle

s = 'aa bb cc'

print(''.join(s.split()))

print(s.replace(' ', ''))


lst = [1, 2, 3, 4]

shuffle(lst)
print(lst)