"""
    task 125
"""
class Solution:
    def getOnlyAlphaNumericPart(self, s: str) -> str:
        alpha_num_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                alpha_num_str += s[i]
        return alpha_num_str

    def isPalindrome(self, s: str) -> bool:
        s = self.getOnlyAlphaNumericPart(s)
        s = s.lower()

        if s == s[::-1]:
            return True
        return False
