from timeit import timeit


def even_values(lst):
    """
    >>> even_values([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> even_values([9, 0, 9, 0, 9])
    [0, 0]
    """
    values = []
    for i, v in enumerate(lst, start=1):
        if not i % 2:
            values.append(v)
    return values


def even_values_better(lst):
    """
    >>> even_values_better([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> even_values_better([9, 0, 9, 0, 9])
    [0, 0]
    """
    return [v for i, v in enumerate(lst, start=1) if not i % 2]


def even_values_best(lst):
    """
    >>> even_values_best([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> even_values_best([9, 0, 9, 0, 9])
    [0, 0]
    """
    return lst[1::2]
