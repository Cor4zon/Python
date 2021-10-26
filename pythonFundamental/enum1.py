"""
iterable - итерируемый
Любой объект, который может возрващать свои элементы по одному.
"""
def enum1():
    lst = ['a', 'b', 'c', 'd', 'e']
    for count, value in enumerate(lst, start=1):
        print(count, value)


def enum2(iterable):
    """Return values from iterable when their index is even"""
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values


def enum3(iterable):
    """Returns values from iterable when their index is even
        This isn't most efficient way
    """
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]


def enum4(iterable):
    """More efficient way
        It doesn't work with generators and iterators (becase they can't be indexed or sliced)
    """
    return list(iterable[1::2])


print(enum3(list(range(1, 11))))
print(enum3(list(range(1, 11))))


alphabet = "abcderfghjiklmnop"
print(enum4(alphabet))


