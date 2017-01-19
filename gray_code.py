class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        nMax = 2 ** n
        return [(x >> 1) ^ x for x in range(nMax)]


s = Solution()
res = s.grayCode(5)
for r in res:
    print "{0:b}".format(r)
