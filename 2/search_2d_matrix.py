class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target < matrix[0][0]:
            return False

        # m row x n col matrix
        m = len(matrix)
        n = len(matrix[0])

        col = n - 1
        row = 0

        while col >= 0 and row < m:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
s = Solution()
print(s.searchMatrix(matrix, 1))
print(s.searchMatrix(matrix, 2))
print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 4))
print(s.searchMatrix(matrix, 5))
print(s.searchMatrix(matrix, 20))
