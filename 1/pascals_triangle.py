class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        res = []
        res.append([1])

        if numRows == 1:
            return res

        for i in xrange(1, numRows):
            length = i + 1
            row = [1 for _ in xrange(length)]
            for j in xrange(1, length - 1):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res


s = Solution()
print s.generate(0)
print s.generate(1)
print s.generate(5)
