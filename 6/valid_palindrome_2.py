class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return s[start:end] == s[start:end][::-1] or s[start+1:end+1] == s[start+1:end+1][::-1]
        return True
