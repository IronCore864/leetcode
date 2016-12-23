class Solution(object):
    def _get_possibilities(self, p, m, n):
        if p[m][n] != -1:
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

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        p = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    p[i][j] = 0
        return self._get_possibilities(p, m - 1, n - 1)


s = Solution()
obstacle = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print s.uniquePathsWithObstacles(obstacle)
