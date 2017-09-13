class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.sum = matrix
        for i in range(1, m):
            self.sum[i][0] = self.sum[i - 1][0] + matrix[i][0]
        for j in range(1, n):
            self.sum[0][j] = self.sum[0][j - 1] + matrix[0][j]

        for i in range(1, m):
            for j in range(1, n):
                self.sum[i][j] = matrix[i][j] + self.sum[i][j - 1] + self.sum[i - 1][j] - self.sum[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        res = self.sum[row2][col2]
        if col1 > 0:
            res -= self.sum[row2][col1 - 1]
        if row1 > 0:
            res -= self.sum[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            res += self.sum[row1 - 1][col1 - 1]
        return res


s = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])
print(s.sumRegion(2, 1, 4, 3))
