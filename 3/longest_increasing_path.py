class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        res = [[0 for _ in range(n)] for _ in range(m)]

        def find_max_path(i, j):
            if res[i][j] != 0:
                return res[i][j]

            tmp_res = 0

            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                tmp_res = max(tmp_res, find_max_path(i, j - 1))

            if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:
                tmp_res = max(tmp_res, find_max_path(i, j + 1))

            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                tmp_res = max(tmp_res, find_max_path(i - 1, j))

            if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:
                tmp_res = max(tmp_res, find_max_path(i + 1, j))

            res[i][j] = 1 + tmp_res

            return res[i][j]

        for i in range(m):
            for j in range(n):
                find_max_path(i, j)

        return max([j for i in res for j in i])


s = Solution()
# m = [[9, 9, 4],
#      [6, 6, 8],
#      [2, 1, 1]]
m = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
res = s.longestIncreasingPath(m)
print(res)
