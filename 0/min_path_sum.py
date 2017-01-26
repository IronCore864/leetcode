class Solution(object):
    def _get_min_path_sum(self, grid, min_sum, m, n):
        if min_sum[m][n] != -1:
            return min_sum[m][n]

        if m == 0 and n == 0:
            min_sum[m][n] = grid[0][0]
            return grid[0][0]
        elif m == 0:
            min_sum[m][n] = grid[m][n] + self._get_min_path_sum(grid, min_sum, m, n - 1)
        elif n == 0:
            min_sum[m][n] = grid[m][n] + self._get_min_path_sum(grid, min_sum, m - 1, n)
        else:
            min_sum[m - 1][n] = self._get_min_path_sum(grid, min_sum, m - 1, n)
            min_sum[m][n - 1] = self._get_min_path_sum(grid, min_sum, m, n - 1)
            min_sum[m][n] = grid[m][n] + min(min_sum[m - 1][n], min_sum[m][n - 1])
        return min_sum[m][n]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        min_sum = [[-1 for _ in range(n)] for _ in range(m)]
        return self._get_min_path_sum(grid, min_sum, m - 1, n - 1)


s = Solution()
print s.minPathSum([
    [1, 2, 3],
    [1, 5, 6],
    [1, 1, 1],
])
