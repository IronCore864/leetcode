class Solution(object):
    def _take(self, grid, i, j, m, n):
        grid[i][j] = '0'
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self._take(grid, i - 1, j, m, n)
        if i + 1 < m and grid[i + 1][j] == '1':
            self._take(grid, i + 1, j, m, n)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self._take(grid, i, j - 1, m, n)
        if j + 1 < n and grid[i][j + 1] == '1':
            self._take(grid, i, j + 1, m, n)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                else:
                    self._take(grid, i, j, m, n)
                    count += 1
        return count


s = Solution()
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]
print(s.numIslands(grid))

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]
print(s.numIslands(grid))
