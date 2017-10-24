class Solution(object):
    def helper(self, grid):
        res = 0
        row = len(grid)
        col = len(grid[0])
        grid.insert(0, [0] * col)
        grid.append([0] * col)
        res = 0
        for i in range(row + 1):
            for j in range(col):
                if grid[i][j] != grid[i + 1][j]:
                    res += 1
        return res

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        transpose = zip(*grid)
        return self.helper(grid) + self.helper(transpose)
