from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1 <= m, n <= 300

        After looking at some examples, it's not hard to figure out that:
        we start from one '1' and try to move to the next '1' horizontally and vertically until we can't move anymore
        then it's one island.
        """
        m, n = len(grid), len(grid[0])

        def fill(x, y):
            grid[x][y] = '#'
            if x > 0 and grid[x-1][y] == '1':
                fill(x-1, y)
            if x < m-1 and grid[x+1][y] == '1':
                fill(x+1, y)
            if y > 0 and grid[x][y-1] == '1':
                fill(x, y-1)
            if y < n-1 and grid[x][y+1] == '1':
                fill(x, y+1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    fill(i, j)
                    res += 1

        return res


if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(s.numIslands(grid))
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.numIslands(grid))
