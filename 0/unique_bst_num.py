class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0 for _ in range(n + 1)]
        g[0] = 1
        g[1] = 1
        for i in xrange(2, n + 1):
            for j in range(1, i + 1):
                g[i] += g[j - 1] * g[i - j]
        return g[n]


s = Solution()
print s.numTrees(3)
print s.numTrees(4)
print s.numTrees(5)
