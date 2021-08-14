def isPalindrom(s: str) -> bool:
    if len(s) == 1:
        return True

    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longestPalindrome(s: str) -> str:
    if isPalindrom(s):
        return s
    else:
        left, right = longestPalindrome(s[1:]), longestPalindrome(s[:len(s)-1])
        return left if len(left) > len(right) else right


def f(s: str) -> str:

    i = 0
    s1, s2 = s[i:], s[:len(s)]

    while True:
        if (s1 is None) and (s2 is None):
            break

        s1, s2 = s[i:], s[:len(s)-i]

        if isPalindrom(s1) or isPalindrom(s2):
            break

        i += 1

    if not isPalindrom(s2):
        return s1
    else:
        return s2


# print(longestPalindrome("abbcccbbbcaaccbababcbcabca"))
# print(f('a'))
# print(f('babad'))
# print(f('ac'))
print(f('abbcccbbbcaaccbababcbcabcad'))
# print(longestPalindrome("a"))
# print(longestPalindrome("babad"))
# print(longestPalindrome("ac"))