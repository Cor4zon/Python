def count_unique(s):
    '''
    Count number of characters in s
    >>> count_unique("aabb")
    2
    >>> count_unique('abc')
    3
    '''
    seen_c = []                 # O(1)
    for i in s:                 # O(n)
        if i not in seen_c:     # O(n)
            seen_c.append(i)    # O(1)
    return len(seen_c)          # result: O(n*n)


def count_unique_2(s):
    seen_c = set(s)             # O(1)
    for c in s:                 # O(n)
        if c not in seen_c:     # O(1)
            seen_c.add(c)       # O(1)
    return len(seen_c)          # result: O(n)


# то же, что и функция 2, но аккуратнее
def count_unique_3(s):
    return len({c for c in s})  # O(n)


# то же, что и функция 3
def count_unique_4(s):
    return len(set(s))          # O(n)

