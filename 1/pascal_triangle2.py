class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        res = [1]

        for i in xrange(1, rowIndex + 1):
            for j in xrange(len(res) - 1, 0, -1):
                res[j] = res[j] + res[j - 1]
            res.append(1)
        return res


s = Solution()
print s.getRow(0)
print s.getRow(1)
print s.getRow(2)
print s.getRow(3)
print s.getRow(4)
print s.getRow(5)