class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        for i in xrange(1, len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                remaining = self.partition(s[i:])
                if i == len(s):
                    res.append([s[:i]])
                elif remaining:
                    res += [[s[:i]] + r for r in remaining]
        return res


s = Solution()
print s.partition('aab')
