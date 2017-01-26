class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == "":
            return 0
        words = s.split(' ')
        return len(words[-1])


s = Solution()
print s.lengthOfLastWord("          ")
print s.lengthOfLastWord("hello world")
print s.lengthOfLastWord(" hello world  ")


