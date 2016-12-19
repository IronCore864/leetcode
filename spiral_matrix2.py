class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1
        for num in range(1, n * n + 1):
            res[i][j] = num
            if di == 0 and dj == 1 and (j == n - 1 or res[i + di][j + dj] != 0):
                di, dj = 1, 0
            elif di == 1 and dj == 0 and (i == n - 1 or res[i + di][j + dj] != 0):
                di, dj = 0, -1
            elif di == 0 and dj == -1 and (i == 0 or res[i + di][j + dj] != 0):
                di, dj = -1, 0
            elif di == -1 and dj == 0 and (i == 0 or res[i + di][j + dj] != 0):
                di, dj = 0, 1
            i, j = i + di, j + dj
        return res


def printMatrix(m):
    for row in m:
        print row


s = Solution()
printMatrix(s.generateMatrix(0))
printMatrix(s.generateMatrix(1))
printMatrix(s.generateMatrix(2))
printMatrix(s.generateMatrix(3))
printMatrix(s.generateMatrix(4))
printMatrix(s.generateMatrix(5))
printMatrix(s.generateMatrix(6))
printMatrix(s.generateMatrix(7))
printMatrix(s.generateMatrix(8))
printMatrix(s.generateMatrix(9))
printMatrix(s.generateMatrix(10))

