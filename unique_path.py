class Solution(object):
    def _get_possibilities(self, p, m, n):
        if p[m][n] != 0:
            return p[m][n]

        if m == 0 and n == 0:
            p[m][n] = 1
        elif m == 0:
            p[m][n - 1] = self._get_possibilities(p, m, n - 1)
            p[m][n] = p[m][n - 1]
        elif n == 0:
            p[m - 1][n] = self._get_possibilities(p, m - 1, n)
            p[m][n] = p[m - 1][n]
        else:
            p[m][n - 1] = self._get_possibilities(p, m, n - 1)
            p[m - 1][n] = self._get_possibilities(p, m - 1, n)
            p[m][n] = p[m - 1][n] + p[m][n - 1]
        return p[m][n]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = [[0 for _ in range(n)] for _ in range(m)]
        return self._get_possibilities(p, m - 1, n - 1)


s = Solution()
print s.uniquePaths(1, 1)
print s.uniquePaths(1, 2)
print s.uniquePaths(2, 1)
print s.uniquePaths(3, 1)
print s.uniquePaths(2, 2)
print s.uniquePaths(2, 3)
print s.uniquePaths(3, 3)
print s.uniquePaths(4, 4)
