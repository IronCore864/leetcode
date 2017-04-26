class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s or len(s) == 0:
            return 0

        n = len(s)

        cut = [i - 1 for i in xrange(n + 1)]

        for i in xrange(n):
            j = 0
            while i + j < n and j <= i and s[i - j] == s[i + j]:
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j])
                j += 1
            j = 1
            while i + j < n and j <= i + 1 and s[i - j + 1] == s[i + j]:
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j + 1])
                j += 1
        return cut[n]


s = Solution()
print s.minCut("cabababcbc")
