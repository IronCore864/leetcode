class Solution:
    def isToeplitzMatrix(self, matrix):
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            cur_i, cur_j = i, 0
            while cur_i < r and cur_j < c:
                if matrix[cur_i][cur_j] != matrix[i][0]:
                    return False
                cur_i, cur_j = cur_i + 1, cur_j + 1

        for j in range(c):
            cur_i, cur_j = 0, j
            while cur_i < r and cur_j < c:
                if matrix[cur_i][cur_j] != matrix[0][j]:
                    return False
                cur_i, cur_j = cur_i + 1, cur_j + 1

        return True


s = Solution()
print(s.isToeplitzMatrix([[36, 59, 71, 15, 26, 82, 87], [56, 36, 59, 71, 15, 26, 82], [15, 0, 36, 59, 71, 15, 26]]))
print(s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
