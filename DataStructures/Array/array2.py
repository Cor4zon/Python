# Найти первое непвторяющееся число в массиве


def search_fisrt_unique(lst):
    """
    >>> search_fisrt_unique([1, 1, 2, 3, 4, 2, 2, 4, 4, 5])
    3
    >>> search_fisrt_unique([])
    None
    >>> search_fisrt_unique([1])
    1
    >>> search_fisrt_unique([1, -1, 1, -1, 1, -1])
    None
    >>> search_fisrt_unique([1, 2, 3])
    1
    """
    for i in range(len(lst)):
        if lst[i] not in lst[i+1:] and lst[i] not in lst[:i]:
            return lst[i]
    return None

