'''
    the actual code for enumerate() is written in C.
'''
import string


def my_enumerate(sequence, start=0):
    """
    1. Accept an iterable and a starting count value as arguments
    2. Send back a tuple with the current count value and the associated item from the iterable
    """
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


print(list(my_enumerate((1, 2, 3, 4, 5), start=1)))
print(list(my_enumerate(f"{string.ascii_lowercase}", start=1)))
