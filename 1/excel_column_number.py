class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        for c in s[::-1]:
            v = ord(c) - 64
            res += v * 26 ** i
            i += 1
        return res


s = Solution()
print s.titleToNumber('AA')