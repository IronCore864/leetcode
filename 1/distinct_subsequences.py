class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0

        if len(s) == len(t):
            return 0 if s != t else 1

        dp = [[0 for _ in xrange(len(t) + 1)] for _ in xrange(len(s) + 1)]

        for j in xrange(len(t) + 1):
            dp[0][j] = 0

        for i in xrange(len(s) + 1):
            dp[i][0] = 1

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(t) + 1):
                if s[i - 1] != t[j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[len(s)][len(t)]


s = Solution()
print s.numDistinct('rabbbit', 'rabbit')
