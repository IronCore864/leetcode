class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        l = 0
        r = m * n - 1
        if target < matrix[l / n][l % n] or target > matrix[r / n][r % n]:
            return False

        if target == matrix[l / n][l % n] or target == matrix[r / n][r % n]:
            return True

        while l < r:
            if target == matrix[l / n][l % n] or target == matrix[r / n][r % n]:
                return True
            middle = (l + r) / 2
            if target == matrix[middle / n][middle % n]:
                return True
            elif target < matrix[middle / n][middle % n]:
                r = middle - 1
            else:
                l = middle + 1
        return False


s = Solution()
print s.searchMatrix(
    [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3
)
