class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])

        first_row_contains_zero = False
        first_col_contains_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_contains_zero = True
                    if j == 0:
                        first_col_contains_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if first_row_contains_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_contains_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


s = Solution()
res = s.setZeroes([
    [0, 0, 0, 5],
    [4, 3, 1, 4],
    [0, 1, 1, 4],
    [1, 2, 1, 3],
    [0, 0, 1, 1]
])
for row in res:
    print row
