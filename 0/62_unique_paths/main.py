class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            res[0][j] = 1
        for i in range(m):
            res[i][0] = 1

        # there are two ways to go to point (i, j):
        # either from (i-1, j), or from (i, j-1)
        # uniquePaths(m, n) = uniquePaths(m-1, n) + uniquePaths(m, n-1)
        # because it's only allowed to move from top to down, or from left to right
        # there is only one way to reach to the points in the first line or column
        # from there we can calculate each points row by row

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i][j-1] + res[i-1][j]

        return res[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
