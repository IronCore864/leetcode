class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        base = 0
        res = []
        while m > 0 and n > 0:
            count = 0
            i, j = base, base
            if m == 1:
                res += [matrix[i][y] for y in range(base, n + base)]
            elif n == 1:
                res += [matrix[x][j] for x in range(base, m + base)]
            else:
                while count < 2 * n + 2 * (m - 2):
                    res.append(matrix[i][j])
                    if 0 <= count < n - 1:
                        j += 1
                    elif n - 1 <= count < n + (m - 2):
                        i += 1
                    elif n + (m - 2) <= count < n + (m - 2) + (n - 1):
                        j -= 1
                    else:
                        i -= 1
                    count += 1
            base += 1
            m -= 2
            n -= 2
        return res


s = Solution()
print s.spiralOrder([])
print s.spiralOrder([[1, 2, 3, 4, 5]])
print s.spiralOrder([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
])
print s.spiralOrder([[1], [2], [3], [4], [5]])
print s.spiralOrder([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
])
print s.spiralOrder([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
])

