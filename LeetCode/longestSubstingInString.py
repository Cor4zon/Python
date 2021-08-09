def lengthOfLongestSubstring(s: str) -> int:
    subString = ""
    maxLen = 0
    i = 0
    while i < len(s):
        if s[i] not in subString:
            subString += s[i]
            i += 1
            continue

        s = s[s.index(s[i])+1:]
        if maxLen < len(subString):
            maxLen = len(subString)
        subString = ""
        i = 0


    if maxLen < len(subString):
        maxLen = len(subString)

    return maxLen



# print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring(""))