class Solution(object):
    @staticmethod
    def _get_next(i, j, n):
        return j, n - i - 1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(0, n / 2):
            for i in range(j, n - j - 1):
                cur_i, cur_j = i, j
                prev_val = matrix[cur_i][cur_j]
                for k in range(4):
                    next_i, next_j = self._get_next(cur_i, cur_j, n)
                    next_bak = matrix[next_i][next_j]
                    matrix[next_i][next_j] = prev_val
                    cur_i, cur_j = next_i, next_j
                    prev_val = next_bak
        for row in matrix:
            print row


s = Solution()
s.rotate(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
)
s.rotate(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
)

