from collections import Counter

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
    return Counter(string).most_common(3)