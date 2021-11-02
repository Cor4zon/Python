# Найти второй минимальный элемент массива
import random


def search_second_max(lst):
    """
    >>> search_second_max([1, 2, 3, 4, 5])
    4
    >>> search_second_max([-1, 1, -1, 1])
    -1
    """
    assert(len(lst) > 0)
    return sorted(set(lst))[-2]


lst = [random.randint(-10, 10) for _ in range(10)]
print(lst)
print(search_second_max(lst))