from collections import defaultdict

def top_three_letters(string):
    '''
    Given a string find the top three most
    frequent letters
    This method should return a list of tuples,
    where the tuple contains the character and the count
    >>> top_three_letters("abbccc")
    [('c', 3), ('b', 2), ('a', 1)]
    >>> top_three_letters("aabbccd")
    [('a', 2), ('b', 2), ('c', 2)]
    '''
    counter = defaultdict(int)
    for c in string:
        counter[c] += 1

    top_three = sorted(
        counter,
        key=lambda k: counter[k],
        reverse=True
    )[:3]

    return [(letter, counter[letter]) for letter in top_three]

