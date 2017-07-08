class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        maxsize = 0

        pre = [0 for _ in range(m)]
        cur = [0 for _ in range(m)]

        for i in range(m):
            pre[i] = int(matrix[i][0])
            maxsize = max(maxsize, pre[i])

        for j in range(1, n):
            cur[0] = int(matrix[0][j])
            maxsize = max(maxsize, cur[0])
            for i in range(1, m):
                if matrix[i][j] == '1':
                    cur[i] = min(cur[i - 1], min(pre[i - 1], pre[i])) + 1
                    maxsize = max(maxsize, cur[i]);
            pre = cur
            cur = [0 for _ in range(m)]

        return maxsize * maxsize


s = Solution()
print(s.maximalSquare(["10100", "10111", "11111", "10010"]))
