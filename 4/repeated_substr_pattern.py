class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1


s = Solution()
print(s.repeatedSubstringPattern('abcdabcdabcdabc'))
